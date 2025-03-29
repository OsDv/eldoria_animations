import manim
from manim import *

class EldoriaTitleScene(Scene):
	def construct(self):
		# Create a solid blue background
		background = Rectangle(
			width=config.frame_width,
			height=config.frame_height,
			fill_color="#22223b",  # Solid blue color
			fill_opacity=1
		)
		background.set_z_index(-1)  # Ensure it stays behind other elements
		self.add(background)

		# Load and display the logo
		logo = SVGMobject("1logo.svg")  # Load the SVG logo
		logo.set_width(6)  # Set the width to make the logo bigger
		logo.move_to(ORIGIN)  # Center the logo

		# Register the font
		font_path = "./fonts/ADAM.CG PRO.otf"
		with register_font(font_path):
			# Create the title text
			title = Text(
				"Ad Astra",
				font_size=120,
				font="ADAM.CG PRO",
				color="#fffedc",
				)
			title.move_to(DOWN * 0.5)  # Move the text slightly downward

			# Load the shape SVG
			shape = SVGMobject("1shape.svg")  # Corrected the SVG file name
			shape.set_width(6)  # Adjust the size of the shape
			shape.next_to(title, UP, buff=0.5)  # Position the shape above the text

		# Fade in the logo
		self.play(FadeIn(logo, run_time=2))
		self.wait(1)  # Pause for a moment

		# Transform the logo into the text
		self.play(Transform(logo, title, run_time=3))

		# Add the shape on top of the text with a drawing animation
		self.play(DrawBorderThenFill(shape, run_time=3))  # Draw the shape SVG

		 # Add an indicate effect to the shape
		self.play(Indicate(shape,scale_factor=1, run_time=2))  # Highlight the shape

		# Pause for a moment
		self.wait(2)

		# Fade out the text and shape
		self.play(FadeOut(logo, run_time=2), FadeOut(shape, run_time=2))