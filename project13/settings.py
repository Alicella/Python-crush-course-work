class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 20

        # How quickly the game speeds up 
        self.speedup_scale_easy = 1.1
        self.initialize_dynamic_settings_easy()

        self.speedup_scale_mid = 1.2
        self.initialize_dynamic_settings_mid()

        self.speedup_scale_hard = 1.3
        self.initialize_dynamic_settings_hard()

        # How quickly the alien point values increase
        self.score_scale = 1.5

    def initialize_dynamic_settings_easy(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50
    
    def initialize_dynamic_settings_mid(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5 * 1.2
        self.bullet_speed = 3.0 * 1.2
        self.alien_speed = 1.0 * 1.2
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 60
    
    def initialize_dynamic_settings_hard(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5 * 1.4
        self.bullet_speed = 3.0 * 1.4
        self.alien_speed = 1.0 * 1.4
        # self.alien_speed = 50.  # test case to finish game fast
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 70

    def increase_speed_easy(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale_easy
        self.bullet_speed *= self.speedup_scale_easy
        self.alien_speed *= self.speedup_scale_easy

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
    
    def increase_speed_mid(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale_mid
        self.bullet_speed *= self.speedup_scale_mid
        self.alien_speed *= self.speedup_scale_mid

        self.alien_points = int(self.alien_points * self.score_scale)
    
    def increase_speed_hard(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale_hard
        self.bullet_speed *= self.speedup_scale_hard
        self.alien_speed *= self.speedup_scale_hard

        self.alien_points = int(self.alien_points * self.score_scale)

