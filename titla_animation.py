import manim
from manim import *
from manim import config
from manim import ParametricFunction, RIGHT, LEFT, PI, np
from manim import SVGMobject

# Set Full HD resolution and 60 FPS
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 15

class EldoriaTitleScene(Scene):
    def construct(self):
        # Register the font
        font_path = "./fonts/Adventure Time Logo.ttf"
        with register_font(font_path):
            # Create the title text with a yellow-to-orange gradient
            title = Text(
                "Eldoria",
                font_size=160,  # Increased font size
                font="Adventure Time Logo",
                gradient=("#eaba49", "#FFA500"),  # Yellow-to-orange gradient
                stroke_width=8,  # Stroke width for glow effect
                stroke_color="#8a5127",  # Stroke color for glow effect
                stroke_opacity=0.7  # Adjust stroke opacity
                # Removed disable_ligatures=True
            )
            
            # Center the title
            title.move_to(UP * 0)
            
        

            # Add writing animation for the title and underline in parallel
            underline = Underline(title, color=BLUE,
                                stroke_width=8,
                                sheen_factor=-0.5)
            self.play(
                manim.Write(title, run_time=3),
                manim.Write(underline, run_time=6)  # Slower underline animation
            )
            # Removed or reduced wait time            
            # Add bounce effect for the title
            # self.play(title.animate.scale(1.2).set_color("#eaba49"))  # Old code commented out
            self.play(title.animate.scale(1.2),
                      underline.animate.scale(1.2))  # Retain gradient color
            self.play(title.animate.scale(1 / 1.2),
                      underline.animate.scale(1 / 1.2))
        
            # Fade out the logo, title, and underline together
            self.play(FadeOut(title), FadeOut(underline))

