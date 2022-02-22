from manim import *

class Card(Scene):
    def construct(self):
        # root2.txt contains many digits of sqrt(2)
        with open('root2.txt') as root2:
            # background root 2 uses gradient to draw attention to center
            bg_root2 = (
                Text(root2.read())
                .scale_to_fit_width(config['frame_width'])
                .to_corner(LEFT + UP)
                .shift(UP * config['frame_width'] * 0.25)
                .shift(LEFT * 0.5)
                .set_color_by_gradient(ORANGE, YELLOW_E, ORANGE)
                .set_opacity(0.3)
            )

            self.add(bg_root2)

        date = (
            Text('2-22-22', color=YELLOW_D)
            .scale(3)
            .shift(UP)
        )

        # hyphens are a faded yellow compared to the 2s
        date[1].set_color(YELLOW_B)
        date[4].set_color(YELLOW_B)

        self.add(date)

        # using markup text to have a segment of the string be a different color
        message = (
            MarkupText(
                f'Happy <span fgcolor="{YELLOW_D}">Twos</span>day!',
                color=YELLOW_B
            )
            .scale(2)
            .shift(DOWN)
        )

        self.add(message)

