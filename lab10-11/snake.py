import pygame 
import sys 
import random 
import psycopg2

# ИНИЦИАЛИЗАЦИЯ
pygame.init() 
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0) 
RED = (255, 0, 0) 
ORANGE = (255, 165, 0)

snake_pos = [[100, 50], [90, 50], [80, 50]] 
snake_speed = [10, 0] 
food = {'pos': [0, 0], 'weight': 1, 'spawn_time': 0} 
food_spawn = True 
score = 0 
level = 1 
speed_increase = 1  # увеличено для заметного ускорения
food_counter = 0   

fps = pygame.time.Clock() 
paused = False 

# Создание таблицы
def init_db():
    conn = psycopg2.connect(dbname='snake_game', user='postgres', password='1234', host='localhost', port='5432') 
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS snake_game_scores (
            id SERIAL PRIMARY KEY,
            player_name VARCHAR(100),
            score INT,
            level INT
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

# Сохранение очков
def insert_score(name, score, level): 
    conn = psycopg2.connect(dbname='snake_game', user='postgres', password='1234', host='localhost', port='5432') 
    cur = conn.cursor() 
    insert_query = "INSERT INTO snake_game_scores (player_name, score, level) VALUES (%s, %s, %s)" 
    cur.execute(insert_query, (name, score, level)) 
    conn.commit() 
    cur.close() 
    conn.close() 

# Получение очков
def get_scores(name): 
    conn = psycopg2.connect(dbname='snake_game', user='postgres', password='1234', host='localhost', port='5432') 
    cur = conn.cursor() 
    query = "SELECT score, level FROM snake_game_scores WHERE player_name = %s ORDER BY score DESC" 
    cur.execute(query, (name,)) 
    results = cur.fetchall() 
    cur.close() 
    conn.close() 
    return results 

init_db()

# Имя игрока
player_name = input("Enter your name: ").strip()
scores = get_scores(player_name) 
if scores: 
    print("Your previous scores:") 
    for score_row, level_row in scores: 
        print(f"Score: {score_row}, Level: {level_row}") 

# Столкновения
def check_collision(pos): 
    if pos[0] < 0 or pos[0] > SCREEN_WIDTH - 10 or pos[1] < 0 or pos[1] > SCREEN_HEIGHT - 10: 
        return True 
    if pos in snake_pos[1:]: 
        return True 
    return False 

# Новая еда
def get_random_food(): 
    global food_counter 
    while True: 
        pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10] 
        if pos not in snake_pos: 
            weight = 2 if food_counter >= 2 else 1 
            food_counter = 0 if weight == 2 else food_counter + 1 
            return {'pos': pos, 'weight': weight, 'spawn_time': pygame.time.get_ticks()} 

# Основной цикл
try: 
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                insert_score(player_name, score, level)
                print(f"💾 Game closed. Score: {score}, Level: {level} — saved for {player_name}")
                pygame.quit()
                sys.exit()
 
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_UP and snake_speed[1] == 0: 
                    snake_speed = [0, -10] 
                elif event.key == pygame.K_DOWN and snake_speed[1] == 0: 
                    snake_speed = [0, 10] 
                elif event.key == pygame.K_LEFT and snake_speed[0] == 0: 
                    snake_speed = [-10, 0] 
                elif event.key == pygame.K_RIGHT and snake_speed[0] == 0: 
                    snake_speed = [10, 0] 
                elif event.key == pygame.K_p: 
                    paused = not paused 

        if not paused: 
            # движение
            new_head = [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]]
            snake_pos.insert(0, new_head)

            # столкновение
            if check_collision(new_head): 
                insert_score(player_name, score, level)
                print(f"Game over. Score: {score}, Level: {level} — saved for {player_name}")
                pygame.quit() 
                sys.exit()
 

            # еда
            if new_head == food['pos']: 
                score += food['weight'] 
                if score % 3 == 0: 
                    level += 1 
                food = get_random_food()  # сразу создаём новую еду
            else: 
                snake_pos.pop() 

            # еда протухла
            if pygame.time.get_ticks() - food['spawn_time'] > 10000: 
                food = get_random_food()

        # отрисовка
        screen.fill(BLACK)

        # сначала еда
        food_color = RED if food['weight'] == 1 else ORANGE 
        pygame.draw.rect(screen, food_color, pygame.Rect(food['pos'][0], food['pos'][1], 10, 10)) 

        # потом змейка
        for pos in snake_pos: 
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10)) 

        # текст
        font = pygame.font.SysFont('arial', 20) 
        score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE) 
        screen.blit(score_text, [10, 10]) 

        if paused: 
            pause_text = font.render("Paused", True, WHITE) 
            screen.blit(pause_text, [SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2]) 

        pygame.display.flip() 
        fps.tick(10 + level * speed_increase) 

except SystemExit: 
    pygame.quit()