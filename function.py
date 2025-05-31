from data import *
import pygame

TOWER_UPGRADES = {
    "turret": {
        1: {
            "damage": 2,
            "speed": 1.0,
            "radius": 60,
            "can_see_shadow": False,
            "description": "1 урон → 2 урона\n1.0 сек → 0.8 сек"
        },
        2: {
            "damage": 5,
            "speed": 0.5,
            "radius": 80,
            "can_see_shadow": True,
            "description": "2 урона → 5 урона\n+видимость теневых зомби"
        },
        3: {
            "damage": 8,
            "speed": 0.4,
            "radius": 100,
            "can_see_shadow": True,
            "description": "5 урона → 8 урона\n+дальность"
        }
    }
}


class Tower:
    def __init__(self, x, y, image, name, damage, radius, speed, cost, can_see_shadow=False, level=1):
        self.x = x
        self.y = y
        self.image = image
        self.name = name
        self.damage = damage
        self.radius = radius
        self.speed = speed
        self.cost = cost
        self.level = level
        self.can_see_shadow = can_see_shadow
        self.selected = False

        self.last_shot = pygame.time.get_ticks()
        self.range_circle = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.range_circle, (0, 0, 255, 50), (radius, radius), radius)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
        if self.selected:
            # Рисуем радиус, если башня выбрана
            surface.blit(self.range_circle, (self.x + self.image.get_width() // 2 - self.radius,
                                             self.y + self.image.get_height() // 2 - self.radius))

    def is_clicked(self, pos):
        rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return rect.collidepoint(pos)

    def upgrade(self):
        self.level += 1
        self.damage += 5
        self.radius += 10
        self.speed *= 0.9
        self.range_circle = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.range_circle, (0, 0, 255, 50), (self.radius, self.radius), self.radius)
    


class Enemy:
    def __init__(self, x, y, width, height, image, hp=100, speed=1, reward=5, is_shadow=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.hp = hp
        self.max_hp = hp
        self.speed = speed
        self.reward = reward
        self.is_shadow = is_shadow
        self.path = []
        self.path_index = 0
        self.alive = True

    def set_path(self, path):
        self.path = path

    def move(self):
        if self.path_index < len(self.path):
            target_x, target_y = self.path[self.path_index]
            dx = target_x - self.x
            dy = target_y - self.y
            dist = (dx ** 2 + dy ** 2) ** 0.5
            if dist < self.speed:
                self.x, self.y = target_x, target_y
                self.path_index += 1
            else:
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        pygame.draw.rect(window, RED, (self.x, self.y - 10, self.width, 5))
        pygame.draw.rect(window, GREEN, (self.x, self.y - 10, self.width * (self.hp / self.max_hp), 5))


def generate_path_from_map(map_data):
    path = []
    visited = set()

    # Найти самую левую "1" по всей карте
    start_x, start_y = None, None
    for x in range(len(map_data[0])):
        for y in range(len(map_data)):
            if map_data[y][x] == "1":
                start_x, start_y = x, y
                break
        if start_x is not None:
            break

    if start_x is None or start_y is None:
        return []  # если путь не найден

    path.append((start_x * 20, start_y * 20))
    visited.add((start_x, start_y))

    # 4 направления: вправо, вниз, влево, вверх
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while True:
        x, y = path[-1][0] // 20, path[-1][1] // 20
        found = False
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(map_data) and 0 <= nx < len(map_data[0]):
                if map_data[ny][nx] == "1" and (nx, ny) not in visited:
                    path.append((nx * 20, ny * 20))
                    visited.add((nx, ny))
                    found = True
                    break
        if not found:
            break

    return path


class TowerMenu:
    def __init__(self, x, y, tower_icons):
        self.x = x
        self.y = y
        self.width = 180
        self.height = 100
        self.tower_icons = tower_icons  # [(name, image), ...]
        self.button_size = 48
        self.visible = False
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.set_alpha(230)
        self.surface.fill((50, 50, 50))

    def draw(self, screen):
        if not self.visible:
            return
        screen.blit(self.surface, (self.x, self.y))
        for i, (name, icon) in enumerate(self.tower_icons):
            screen.blit(pygame.transform.scale(icon, (self.button_size, self.button_size)),
                        (self.x + 10 + i * (self.button_size + 10), self.y + 25))

    def is_button_clicked(self, pos):
        if not self.visible:
            return None
        for i, (name, icon) in enumerate(self.tower_icons):
            bx = self.x + 10 + i * (self.button_size + 10)
            by = self.y + 25
            if pygame.Rect(bx, by, self.button_size, self.button_size).collidepoint(pos):
                return name
        return None

    def open(self, x, y):
        self.x = x
        self.y = y
        self.visible = True

    def close(self):
        self.visible = False

    def is_open(self):
        return self.visible

    def is_inside(self, pos):
        return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(pos)
    

        
