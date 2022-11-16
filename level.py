from tokenize import group
import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug 
from support import *
from random import choice, random
from weapon import Weapon
from ui import UI
from enemy import Enemy

class Level:
	def __init__(self):
		
		# get display surface 
		self.display_surface = pygame.display.get_surface()
		
		# sprite group setup 
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		#attack sprites
		self.current_attack = None

		# sprite setup 
		self.create_map()

		#user interface 
		self.ui = UI()

	def create_map(self):
		layouts = {
			#'boundary': import_csv_layout('./map/map_FloorBlocks.csv'),
			'boundary': import_csv_layout('./map/marshmapMkII_ground.csv'),
			'grass': import_csv_layout('./map/map_Grass.csv'),
			'object': import_csv_layout('./map/map_Objects.csv'),
			'entities': import_csv_layout('./map/map_Entities.csv')
		}
		grpahics = {
			'grass': import_folder('./graphics/grass'),
			'objects': import_folder('./graphics/objects'),
		}

		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						
						#creating invisible boundary tiles 
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites],'invisible')
						
						#creating grass tiles 
						if style == 'grass':
							random_grass_image = choice(grpahics['grass'])
							Tile((x,y),[self.visible_sprites, self.obstacle_sprites],'grass',random_grass_image)				
						
						if style == 'object':
							surf = grpahics['objects'][int(col)]
							Tile((x,y),[self.visible_sprites, self.obstacle_sprites],'objects',surf)
						
						if style == 'entities':
							if col == '394':
								self.player = Player(
									(x,y),
									[self.visible_sprites],
									self.obstacle_sprites,
									self.create_attack,
									self.destroy_attack,
									self.create_magic)
							else:
								if col == '390': monster_name = 'bamboo'
								elif col == '391': monster_name = 'spirit'
								elif col == '392': monster_name = 'raccoon'
								else: monster_name = 'squid'
								Enemy(monster_name,(x,y),[self.visible_sprites],self.obstacle_sprites)

	def create_attack(self):
		self.current_attack = Weapon(self.player,[self.visible_sprites])
	
	def create_magic(self,style,strength,cost):
		print(style)
		print(strength)
		print(cost)

	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None

	def run(self):
		# update and draw game 
		self.visible_sprites.custom_draw(self.player)
		self.visible_sprites.update()
		self.visible_sprites.enemy_update(self.player)
		self.ui.display(self.player)
		#debug(self.player.status)

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		#general setup
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		#creating the floor 
		#self.floor_surf = pygame.image.load('./graphics/tilemap/ground.png')
		self.floor_surf = pygame.image.load('./graphics/tilemap/MarshMapMkII.png')
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self,player):
		#getting offset
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		#drawing the floor 
		floor_offset_pos = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surf,floor_offset_pos)

		#for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)

	def enemy_update(self,player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)
