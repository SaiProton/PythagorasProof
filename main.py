from manim import *

from math import sqrt

class Pythag(Scene):
    def construct(self):
        self.box_scale = 2 

        self.plane()
        self.triangle()
        self.multi_triangle()
        self.box_proof1()
        self.box_proof2()
        self.root2()

    def plane(self):
        self.fw = config['frame_width']

        # each unit of the plane is 1/8th of the frame's width
        self.unit = self.fw / 8

        # initialize a number plane for a clear sense of scale
        self.number_plane = NumberPlane(
            x_range=[-self.box_scale, self.box_scale, 1],
            y_range=[-self.box_scale, self.box_scale, 1],

            x_length=self.fw * 1.5,
            y_length=self.fw * 1.5,

            faded_line_ratio=3,

            background_line_style={
                "stroke_color": YELLOW_B,
                "stroke_width": 4,
                "stroke_opacity": 0.5
            },

            axis_config={
                "stroke_opacity": 0,
            }
        )

        self.scale = 2

        self.add(self.number_plane)
        self.wait(0.5)

        # zoom into the 3rd quadrant area of the plane
        self.play(
            self.number_plane.animate
            .scale(self.scale)
            .move_to(
                [self.unit * self.scale * 1.5, self.unit * self.scale * 1.5, 0]
            )
        )

    def triangle(self):
        self.tri1 = Polygon(
            [0, 0, 0],
            [0, self.unit * self.scale * 3, 0],
            [self.unit * self.scale * 3, 0, 0],
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=0.8,
        )

        self.tri1.move_to([0, 0, 0])

        self.play(
            DrawBorderThenFill(self.tri1),
            run_time=3
        )

        self.wait(0.5)

        # braces and labels for each of the sides of the triangle

        brace_down = Brace(self.tri1, buff=0.5, direction=DOWN)
        brace_left = Brace(self.tri1, buff=0.5, direction=LEFT)

        label_down = brace_down.get_text('1').scale(2)
        label_left = brace_left.get_text('1').scale(2)

        self.play(Write(brace_down), Write(brace_left))
        self.play(Write(label_down), Write(label_left))

        self.wait(0.5)

        brace_hyp = Brace(
            self.tri1,
            buff=0.5,
            direction=[1, 1, 0],
            stroke_color=ORANGE,
            fill_color=ORANGE
        )

        label_hyp = brace_hyp.get_text('?').scale(2).set_color(YELLOW_D)

        # orange line to highlight the hypotonuse of the triangle
        self.hyp_line = Line(
            [0, self.unit * self.scale * 3, 0],
            [self.unit * self.scale * 3, 0, 0],
            stroke_color=ORANGE,
        ).move_to([0, 0, 0])

        self.play(Write(brace_hyp), FadeIn(self.hyp_line))
        self.play(Write(label_hyp))

        self.wait(1)

        self.play(
            Unwrite(brace_down),
            Unwrite(brace_left),
            Unwrite(label_down),
            Unwrite(label_left),
            Unwrite(brace_hyp),
            Unwrite(label_hyp),
            FadeOut(self.hyp_line)
        )

        self.hyp_line.scale(0.5).move_to(
            [self.unit * -1.5, self.unit * -1.5, 0]
        ).set_opacity(0)

        self.wait(0.5)

    def multi_triangle(self):
        # zoom out the plane and center it
        self.play(
            self.number_plane.animate
            .scale(0.5)
            .move_to([0, 0, 0]),

            self.tri1.animate
            .scale(0.5)
            .move_to([self.unit * -1.5, self.unit * -1.5, 0]),
        )

        # creating copies of the triangle and rotating into new positions

        self.tri2 = self.tri1.copy()
        self.play(
            Rotate(
                self.tri2,
                180 * DEGREES,
                rate_func=rate_functions.ease_out_bounce
            ),
        )

        self.tri3 = self.tri2.copy()
        self.play(
            Rotate(
                self.tri3,
                -180 * DEGREES,
                about_point=ORIGIN,
                rate_func=rate_functions.ease_out_elastic,
            )
        )

        self.tri4 = self.tri3.copy()
        self.play(
            Rotate(
                self.tri4,
                180 * DEGREES,
                rate_func=rate_functions.ease_out_bounce
            )
        )

        self.wait(0.5)

    def box_proof1(self):
        # form a red box surrounding the area of 4 units^2
        self.big_box = Square(
            self.unit * 6,
            color=RED,
            stroke_opacity=0,
            fill_color=RED,
            fill_opacity=0.5,
            z_index=-1
        )

        self.play(FadeIn(self.big_box), run_time=1)

        # area of red squares before evaluation
        square_text1 = MathTex('1^2').move_to(
            [self.unit * -1.5, self.unit * 1.5, 0]
        ).scale(3)

        square_text2 = MathTex('1^2').move_to(
            [self.unit * 1.5, self.unit * -1.5, 0]
        ).scale(3)

        # area of red squares after evaluation
        square_text1_eval = MathTex('1').move_to(
            [self.unit * -1.5, self.unit * 1.5, 0]
        ).scale(4)

        square_text2_eval = MathTex('1').move_to(
            [self.unit * 1.5, self.unit * -1.5, 0]
        ).scale(4)

        self.play(Write(square_text1), Write(square_text2))

        self.wait(0.5)

        self.play(
            Transform(square_text1, square_text1_eval),
            Transform(square_text2, square_text2_eval)
        )

        self.wait(1)

        self.play(Unwrite(square_text1), Unwrite(square_text2))

        self.wait(1)

    def box_proof2(self):
        # rotating two triangles to form a big square in the center
        self.play(
            Rotate(
                self.tri2,
                -90 * DEGREES,
                about_point=[0, self.unit * -3, 0],
                rate_func=rate_functions.ease_out_bounce,
            ),

            Rotate(
                self.tri3,
                -90 * DEGREES,
                about_point=[0, self.unit * 3, 0],
                rate_func=rate_functions.ease_out_bounce
            ),

            run_time=1.5
        )

        self.wait(0.5)

        # equation in progressing states of evaluation
        self.square_text = MathTex('1^2 + 1^2').scale(4)
        square_text_eval1 = MathTex('1 + 1').scale(4)
        square_text_eval2 = MathTex('2').scale(5)

        self.play(Write(self.square_text))
        self.wait(0.5)

        self.play(Transform(self.square_text, square_text_eval1))
        self.wait(0.5)

        self.play(Transform(self.square_text, square_text_eval2))
        self.wait(1)

    def root2(self):
        # hyp of triangle
        offset = sqrt(2 * 1.5**2)

        # vertical addition before rotation
        addition = 2

        # rotating each Mobject currently on the screen during the end scene
        # everything but the beginning triangle is set to disappear
        self.play(
            self.tri1.animate
            .move_to([0, self.unit * (-offset + addition), 0])
            .rotate(45 * DEGREES)
            .set_opacity(0.8),

            self.tri2.animate
            .move_to([self.unit * offset, self.unit * addition, 0])
            .rotate(45 * DEGREES)
            .set_opacity(0),

            self.tri3.animate
            .move_to([self.unit * -offset, self.unit * addition, 0])
            .rotate(45 * DEGREES)
            .set_opacity(0),

            self.tri4.animate
            .move_to([0, self.unit * (offset + addition), 0])
            .rotate(45 * DEGREES)
            .set_opacity(0),

            self.hyp_line.animate
            .move_to([0, self.unit * (-offset + addition), 0])
            .rotate(45 * DEGREES)
            .set_opacity(1),

            self.big_box.animate
            .move_to([0, self.unit * addition, 0])
            .rotate(45 * DEGREES)
            .set_opacity(0),

            self.number_plane.animate
            .move_to([0, self.unit * addition, 0])
            .rotate(45 * DEGREES)
            .set_opacity(0),

            self.square_text.animate
            .move_to([0, self.unit * addition / 2, 0])
            .scale(0.75),

            run_time=5
        )

        brace = Brace(self.tri1, direction=UP, buff=0.5, fill_color=ORANGE)

        root = (
            brace.get_tex('\sqrt{2}')
            .set_color(YELLOW_D)
            .scale(2)
            .shift(UP / 2)
        )

        self.play(Write(brace))
        self.play(Transform(self.square_text, root))

        self.wait(5)

