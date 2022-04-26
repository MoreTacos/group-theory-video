from manim import *

class Scene0(Scene):
    def construct(self):
        self.wait(1)

        green1 = "#00a359"
        green2 = "#00b764"
        green3 = "#00e17b"
        green4 = "#00ff8b"

        l1 = VGroup(
            Square(1, color=green1, fill_opacity=1),
            Square(1, color=green1, fill_opacity=1),
            Square(1, color=green1, fill_opacity=1),
            Square(1, color=green1, fill_opacity=1),
        ).arrange(DOWN)

        l2 = VGroup(
            Square(1, color=green2, fill_opacity=1),
            Square(1, color=green2, fill_opacity=1),
            Square(1, color=green2, fill_opacity=1),
        ).arrange(DOWN)

        l3 = VGroup(
            Square(1, color=green3, fill_opacity=1),
            Square(1, color=green3, fill_opacity=1),
        ).arrange(DOWN)

        l4 = VGroup(
            Square(1, color=green4, fill_opacity=1),
        ).arrange(DOWN)

        logo = VGroup(l1, l2, l3, l4).arrange(RIGHT).move_to(ORIGIN + UP)

        t1 = MathTex(r"\text{Davide Radaelli}").scale(2)
        t1.next_to(logo, DOWN)
        self.play(Create(logo), Write(t1), run_time=3)
        self.wait(3)

class Scene1(Scene):
    def construct(self):
        self.wait(1)

        t1 = MathTex(r"\text{Group Theory}").scale(2)
        self.play(Write(t1), run_time=1.5)
        self.wait(3)

        t2 = MathTex(r"\left( ", r"G", r", ", r"\circ", r"\right)").shift(LEFT*4).scale(2).shift(UP*0.5)
        t3 = MathTex(r"""
                     &\to \text{associativity} \\ 
                     &\to \text{neutral element} \\ 
                     &\to \text{inverses}""").next_to(t2, DOWN, MED_LARGE_BUFF)
        self.play(t1.animate.shift(UP*3).scale(0.7))
        self.wait(2)
        self.play(Write(t2), Write(t3))
        self.wait(3)
        self.play(Indicate(t2[1]))
        self.wait(1)
        self.play(Indicate(t2[3]))
        self.wait(1.5)

        t1 = TriangleGroup().with_top().with_right().with_left().shift(RIGHT*4 + DOWN*0.6).scale(2)
        t2 = MathTex(r"\text{Symmetry}").next_to(t1, DOWN)
        self.wait(3)
        self.play(Create(t1.get_mobject()), run_time=2)
        self.wait(0.1)
        self.play(Create(t1.submobjects[0]), run_time=0.6)
        self.play(Create(t1.submobjects[1]), run_time=0.6)
        self.play(Create(t1.submobjects[2]), run_time=0.6)
        self.wait(0.5)
        self.play(Write(t2), run_time=2)
        self.wait(3)


        a1 = MathTex(r"\Leftrightarrow", font_size=144)
        q1 = Text("?", font_size=64)
        a1.shift(DOWN)
        self.wait(1)
        self.play(Write(a1), Write(q1))
        self.wait(4)

class Scene2(Scene):
    def construct(self):
        self.wait(1)
        t1 = MathTex(r"\text{intuitive} \Rightarrow \text{rigorous}").scale(2)
        self.play(Write(t1), run_time=2)
        self.wait(2)
        self.play(FadeOut(t1))

        t1 = TriangleGroup().scale(2.7).shift(LEFT*2.7)
        t2 = MathTex(r"&\to \text{top flip} \\", 
                     r"&\to \text{left flip} \\",
                     r"&\to \text{right flip} \\",
                     r"&\to \text{rotate 120} \\",
                     r"&\to \text{rotate 240} \\",
                     r"&\to \text{do nothing}").next_to(t1, RIGHT, 2.7)
        self.play(Create(t1))
        self.wait(2)
        self.play(Write(t2[0]), t1.flip_top())
        self.wait(1)
        self.play(Write(t2[1]), t1.flip_left())
        self.wait(1)
        self.play(Write(t2[2]), t1.flip_right())
        self.wait(2)
        self.play(Write(t2[3]), t1.rotate120())
        self.wait(1)
        self.play(Write(t2[4]), t1.rotate240())
        self.wait(2)
        self.play(Write(t2[5]), t1.do_nothing())
        self.wait(1)

        t3 = MathTex(r"\text{Symmetry?}").scale(2).shift(UP*3)
        self.play(t1.animate.shift(DOWN), t2.animate.shift(DOWN))
        self.play(Write(t3))
        self.wait(2)

class Scene3(Scene):
    def construct(self):
        self.wait(1.5)
        t1 = Text("duality", gradient=(RED, ORANGE), font_size=142)
        self.play(Write(t1), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(t1))
        self.wait(2)

class Scene4(Scene):
    def construct(self):
        self.wait(1)
        t1 = MathTex(r"\text{adjective}").scale(1.2)
        t2 = MathTex(r"\text{verb}").scale(1.2)
        VGroup(t1, t2).arrange(RIGHT, 6).move_to(ORIGIN).shift(UP*1.8)
        t3 = TriangleGroup().with_top().with_right().with_left().scale(1.8).next_to(t1, DOWN, MED_LARGE_BUFF)
        t4 = Text(r'"That triangle is very symmetric"').scale(0.5).next_to(t3, DOWN, MED_SMALL_BUFF)
        self.play(Write(t1))
        self.wait(1)
        triangle = t3.get_mobject()
        self.play(Create(triangle), run_time=2)
        self.play(Create(t3.submobjects[0]), run_time=0.8)
        self.play(Create(t3.submobjects[1]), run_time=0.8)
        self.play(Create(t3.submobjects[2]), run_time=0.8)
        self.wait(2)
        self.play(Write(t4))
        self.wait(1)
        self.play(FadeOut(t4))
        self.wait(1)


        total = VGroup(Text(r"fliptop(x)"), 
                       Text(r"flipright(x)"), 
                       Text(r"flipleft(x)"), 
                       Text(r"rotate120(x)"), 
                       Text(r"rotate240(x)"), 
                       Text(r"donothing(x)")).arrange(DOWN).scale(0.7)
        total.next_to(t2, DOWN, MED_LARGE_BUFF)
        b1 = Brace(total, direction=LEFT).scale(1.07)
        b2 = Brace(total, direction=RIGHT).scale(1.07)

        self.wait(1)
        self.play(Write(t2))
        self.wait(2)
        self.play(FadeIn(total))
        self.wait()
        self.play(FadeIn(b1), FadeIn(b2))
        self.wait(2)

        t5 = MathTex(r"\text{Instrinsic Symmetries}").move_to(t1)
        middle = np.array((ORIGIN[0], b1.get_left()[1], 0))
        t6 = MathTex(r"\Rightarrow").scale(2.7).move_to(middle)
        t7 = MathTex(r"\text{Set of Symmetries}").move_to(t2)

        self.play(ReplacementTransform(t1, t5))
        self.play(Write(t6))
        self.play(ReplacementTransform(t2, t7))
        self.wait(6)
        self.play(FadeOut(t3, t6, t5, t7, total, b1, b2))
        self.play(triangle.animate.move_to(ORIGIN + DOWN*0.7).scale(1.2))
        self.wait(1)

        t1 = MathTex(r"\text{rotate120}", r"\circ", r"\text{rotate240}", r"=", r"\text{donothing}").shift(UP*2.7).scale(1.2)
        bb1 = SurroundingRectangle(t1[0])
        bb2 = SurroundingRectangle(t1[2])
        bb3 = SurroundingRectangle(t1[4])

        self.play(Write(t1))
        self.play(triangle.rotate120(), Create(bb1))
        self.play(triangle.rotate240(), ReplacementTransform(bb1, bb2))
        self.wait(1)
        self.play(triangle.do_nothing(), ReplacementTransform(bb2, bb3))
        self.play(FadeOut(bb3))
        self.wait(2)

        t2 = MathTex(r"\text{fliptop}", r"\circ", r"\text{flipright}", r"\circ", r"\text{rotate240}", r"=", r"\text{rotate120}").shift(UP*2.7).scale(1.2)
        bb1 = SurroundingRectangle(t2[0])
        bb2 = SurroundingRectangle(t2[2])
        bb3 = SurroundingRectangle(t2[4])
        bb4 = SurroundingRectangle(t2[6])

        self.play(ReplacementTransform(t1, t2))
        self.wait(1)
        self.play(triangle.flip_top(), Create(bb1))
        self.play(triangle.flip_right(), ReplacementTransform(bb1, bb2))
        self.play(triangle.rotate240(), ReplacementTransform(bb2, bb3))
        self.wait(1)
        self.play(triangle.rotate120(), ReplacementTransform(bb3, bb4))
        self.wait(1)
        self.play(FadeOut(bb4))
        self.wait(2)

        t1 = MathTex(r"\left( \text{symmetries, composition} \right) \text{ is a group}").move_to(t2).scale(1.2)
        self.play(ReplacementTransform(t2, t1), triangle.animate.shift(DOWN*0.6))
        self.wait(1)

        t21 = MathTex("1.")
        t2 = MathTex(r"\left( a\circ b \right)\circ c = a \circ \left( b\circ c \right)")
        t2 = VGroup(t21, t2)
        t2.arrange(RIGHT, 0.5)
        t2.next_to(t1, DOWN)
        t3 = MathTex(r"\text{neutral} \circ a = a")
        t31 = MathTex("2.")
        t3 = VGroup(t31, t3)
        t3.arrange(RIGHT, 0.5)
        t3.next_to(t1, DOWN)
        t4 = MathTex(r"a \circ a^{-1} = \text{neutral}")
        t41 = MathTex("3.")
        t4 = VGroup(t41, t4)
        t4.arrange(RIGHT, 0.5)
        t4.next_to(t1, DOWN)
        self.play(Write(t2))
        self.play(triangle.flip_right())
        self.play(triangle.rotate240())
        self.play(triangle.do_nothing())
        self.play(triangle.flip_left())
        self.wait(2)
        self.play(ReplacementTransform(t2, t3))
        self.wait(1)
        self.play(triangle.do_nothing(), run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(t3, t4))
        self.play(triangle.rotate120())
        self.play(triangle.rotate240())
        self.wait(1)
        self.play(triangle.flip_top())
        self.play(triangle.flip_top())
        self.wait(2)

class TriangleGroup(RegularPolygon):
    def __init__(self, **kwargs):
        super().__init__(n=3, **kwargs)
    def get_mobject(self):
        temp = self.copy()
        temp.submobjects = []
        return temp
    def with_top(self):
        triangle = self.get_mobject()
        sym = DashedLine(triangle.get_top(), triangle.get_bottom())
        sym.scale(1.2)
        return self.add(sym)
    def flip_top(self):
        sym = DashedLine(self.get_bottom(), self.get_top())
        sym.scale(1.2)
        a1 = FadeIn(sym, run_time=0.5)
        a2 = self.animate.flip(UP, about_point=self.get_center_of_mass())
        a3 = FadeOut(sym, run_time=0.5)
        a0 = AnimationGroup(a1, a2, lag_ratio=0.25, run_time=2)
        return Succession(a0, a3)
    def with_right(self):
        triangle = self.get_mobject()
        vertex = np.array((triangle.get_right()[0], triangle.get_bottom()[1], 0.0))
        midpoint = np.array(((triangle.get_left()[0] + triangle.get_top()[0])/2, (triangle.get_bottom()[1] + triangle.get_top()[1])/2, 0.0))
        sym = DashedLine(vertex, midpoint)
        sym.scale(1.2)
        return self.add(sym)
    def flip_right(self):
        vertex = np.array((self.get_right()[0], self.get_bottom()[1], 0.0))
        midpoint = np.array(((self.get_left()[0] + self.get_top()[0])/2, (self.get_bottom()[1] + self.get_top()[1])/2, 0.0))
        sym = DashedLine(vertex, midpoint)
        sym.scale(1.2)
        a1 = FadeIn(sym, run_time=0.5)
        a2 = self.animate.flip(DOWN + RIGHT*1.732051, about_point=self.get_center_of_mass())
        a3 = FadeOut(sym, run_time=0.5)
        a0 = AnimationGroup(a1, a2, lag_ratio=0.25, run_time=2)
        return Succession(a0, a3)
    def with_left(self):
        triangle = self.get_mobject()
        vertex = np.array((triangle.get_left()[0], triangle.get_bottom()[1], 0.0))
        midpoint = np.array(((triangle.get_right()[0] + triangle.get_top()[0])/2, (triangle.get_bottom()[1] + triangle.get_top()[1])/2, 0.0))
        sym = DashedLine(vertex, midpoint)
        sym.scale(1.2)
        return self.add(sym)
    def flip_left(self):
        vertex = np.array((self.get_left()[0], self.get_bottom()[1], 0.0))
        midpoint = np.array(((self.get_right()[0] + self.get_top()[0])/2, (self.get_bottom()[1] + self.get_top()[1])/2, 0.0))
        sym = DashedLine(vertex, midpoint)
        sym.scale(1.2)
        a1 = FadeIn(sym, run_time=0.5)
        a2 = self.animate.flip(DOWN + LEFT*1.732051, about_point=self.get_center_of_mass())
        a3 = FadeOut(sym, run_time=0.5)
        a0 = AnimationGroup(a1, a2, lag_ratio=0.25, run_time=2)
        return Succession(a0, a3)
    def with_rotate120(self):
        triangle = self.get_mobject()
        radius = triangle.get_top()[1] - triangle.get_center_of_mass()[1]
        arrow = Arc(radius*1.3, start_angle=90 * DEGREES, angle=-DEGREES*120, num_components=9, arc_center=triangle.get_center_of_mass())
        from manim.mobject.geometry.tips import ArrowTriangleFilledTip
        tip = ArrowTriangleFilledTip(color=WHITE)
        arrow.add_tip(tip)
        return self.add(arrow)
    def rotate120(self):
        radius = self.get_top()[1] - self.get_center_of_mass()[1]
        arrow = Arc(radius*1.3, start_angle=90 * DEGREES, angle=-DEGREES*120, num_components=9, arc_center=self.get_center_of_mass())
        from manim.mobject.geometry.tips import ArrowTriangleFilledTip
        tip = ArrowTriangleFilledTip(color=WHITE)
        arrow.add_tip(tip)
        a1 = FadeIn(arrow, run_time=0.5)
        a2 = self.animate.rotate(-120*DEGREES, about_point=self.get_center_of_mass())
        a3 = FadeOut(arrow, run_time=0.5)
        a0 = AnimationGroup(a1, a2, lag_ratio=0.25, run_time=2)
        return Succession(a0, a3)
    def with_rotate240(self):
        triangle = self.get_mobject()
        radius = triangle.get_top()[1] - triangle.get_center_of_mass()[1]
        arrow = Arc(radius*1.3, start_angle=90 * DEGREES, angle=DEGREES*120, num_components=9, arc_center=triangle.get_center_of_mass())
        from manim.mobject.geometry.tips import ArrowTriangleFilledTip
        tip = ArrowTriangleFilledTip(color=WHITE)
        arrow.add_tip(tip)
        return self.add(arrow)
    def rotate240(self):
        radius = self.get_top()[1] - self.get_center_of_mass()[1]
        arrow = Arc(radius*1.3, start_angle=90 * DEGREES, angle=DEGREES*120, num_components=9, arc_center=self.get_center_of_mass())
        from manim.mobject.geometry.tips import ArrowTriangleFilledTip
        tip = ArrowTriangleFilledTip(color=WHITE)
        arrow.add_tip(tip)
        a1 = FadeIn(arrow, run_time=0.5)
        a2 = self.animate.rotate(120*DEGREES, about_point=self.get_center_of_mass())
        a3 = FadeOut(arrow, run_time=0.5)
        a0 = AnimationGroup(a1, a2, lag_ratio=0.25, run_time=2)
        return Succession(a0, a3)
    def with_do_nothing(self):
        identity = Text("id")
        vertex = np.array((self.get_right()[0], self.get_bottom()[1], 0.0))
        identity.next_to(vertex, RIGHT)
        return self.add(identity)
    def do_nothing(self):
        identity = Text("id")
        vertex = np.array((self.get_right()[0], self.get_bottom()[1], 0.0))
        identity.next_to(vertex, RIGHT)
        a1 = Write(identity, run_time=1)
        a2 = FadeOut(identity, run_time=1)
        return Succession(a1, a2)

class Scene5(Scene):
    def construct(self):
        self.wait(2)
        t1 = MathTex(r"\left( \text{symmetries, composition} \right)").scale(1.2)
        t1.shift(UP*3 + LEFT*3)
        self.play(Write(t1))
        self.wait(10)
        rings_display = MathTex(r"\left( \mathbb{Z}, + \right)").scale(1.5)
        rings_text = MathTex(r"\text{rings}")
        rings = VGroup(rings_display, rings_text)
        rings.arrange(DOWN, 0.2)

        square = Square()
        triangle = Triangle()
        circle = Circle()
        shapes_display = VGroup(square, VGroup(triangle, circle).arrange(DOWN, 0.5))
        shapes_display.arrange(RIGHT, 0.5).scale(0.4)
        shapes_text = MathTex(r"\text{shapes}")
        shapes = VGroup(shapes_display, shapes_text)
        shapes.arrange(DOWN, 0.2)

        torus = Torus().rotate_about_origin(60*DEGREES, RIGHT)
        manifolds_display = VGroup(torus).scale(0.3)
        manifold_text = MathTex(r"\text{manifolds}")
        manifolds = VGroup(manifolds_display, manifold_text)
        manifolds.arrange(DOWN, 0.2)

        axes = Axes(x_range=[-5, 5.3, 1], y_range=[-1.5, 1.5, 1], x_length=5, axis_config={"color": WHITE})
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        functions_display = VGroup(axes, sin_graph).scale(0.45)
        functions_text = MathTex(r"\text{functions}")
        functions = VGroup(functions_display, functions_text)
        functions.arrange(DOWN, 0.2)

        numbers_display = MathTex(r"\left( \mathbb{R}, + \right)").scale(1.5)
        numbers_text = MathTex(r"\text{numbers}")
        numbers = VGroup(numbers_display, numbers_text)
        numbers.arrange(DOWN, 0.2)

        vectorspaces_display = MathTex(r"\left( V, +, \cdot  \right)").scale(1.5)
        vectorspaces_text = MathTex(r"\text{vector}")
        vectorspaces_text2 = MathTex(r"\text{spaces}")
        vectorspaces = VGroup(vectorspaces_display, vectorspaces_text, vectorspaces_text2)
        vectorspaces.arrange(DOWN, 0.2)
        vectorspaces_text.shift(LEFT*0.3)
        vectorspaces_text2.shift(RIGHT*0.1)

        topo_display = MathTex(r"\left( X, \mathcal{O} \right)").scale(1.5)
        topo_text = MathTex(r"\text{topological}")
        topo_text2 = MathTex(r"\text{spaces}")
        topo = VGroup(topo_display, topo_text, topo_text2)
        topo.arrange(DOWN, 0.2)

        groups_display = MathTex(r"\left(G, + \right)").scale(1.5)
        groups_text = MathTex(r"\text{groups}")
        groups = VGroup(groups_display, groups_text)
        groups.arrange(DOWN, 0.2)

        sets_display = MathTex(r"\left\{ 1, 2, 3 \right\}").scale(1.5)
        sets_text = MathTex(r"\text{sets}")
        sets = VGroup(sets_display, sets_text)
        sets.arrange(DOWN, 0.2)

        rings.shift(UP*0.8, LEFT*5.3)
        shapes.shift(LEFT*2.8)
        manifolds.shift(UP*0.5)
        functions.shift(UP*2 + RIGHT*2.9)
        numbers.shift(UP*2 + RIGHT*5.5)
        vectorspaces.shift(LEFT*5 + DOWN*2.4)
        topo.shift(DOWN*2 + RIGHT*5)
        groups.shift(DOWN*2.2 + RIGHT*2.2)
        sets.shift(DOWN*2.5 + LEFT*1.4)
        self.play(FadeIn(functions), run_time=1)
        self.wait(0.3)
        self.play(FadeIn(sets), run_time=1)
        self.wait(0.3)
        self.play(FadeIn(shapes), run_time=1)
        self.wait(0.3)
        self.play(FadeIn(numbers), run_time=1)
        self.wait(2)
        self.play(FadeIn(rings), run_time=1)
        self.wait(0.3)
        self.play(FadeIn(vectorspaces), run_time=1)
        self.wait(0.3)
        self.play(FadeIn(manifolds), run_time=1)
        self.wait(0.3)
        self.play(FadeIn(topo), run_time=1)
        self.wait(0.3)
        self.play(FadeIn(groups), run_time=1)
        self.wait(1)

class Scene6(Scene):
    def construct(self):
        self.wait(2)
        t1 = MathTex(r"\left\{ 1, 2, 3, 4 \right\}").scale(1.5)
        t1.shift(UP*2.8 + LEFT*3.5)

        t2 = VGroup(
            MathTex(r"1\to 2"),
            MathTex(r"2\to 1"),
            MathTex(r"3\to 3"),
            MathTex(r"4\to 4"),
        ).arrange(DOWN, 0.4)
        rect = SurroundingRectangle(t2, color=WHITE, buff=MED_LARGE_BUFF)
        t2.add(SurroundingRectangle(t2, color=WHITE, buff=MED_LARGE_BUFF))

        t3 = VGroup(
            MathTex(r"1\to 1"),
            MathTex(r"2\to 2"),
            MathTex(r"3\to 3"),
            MathTex(r"4\to 3"),
        ).arrange(DOWN, 0.4)
        t3.add(SurroundingRectangle(t3, color=WHITE, buff=MED_LARGE_BUFF))

        t4 = MathTex(r"\left\{ 2, 1, 3, 4 \right\}").scale(1.5)
        t4.shift(DOWN*2.8 + RIGHT*3.5)
        bb0 = SurroundingRectangle(t1, color=GREEN, buff=SMALL_BUFF)
        bb1 = SurroundingRectangle(t4, color=GREEN, buff=SMALL_BUFF)

        t5 = MathTex(r"\left\{ 1, 2, 3 \right\}").scale(1.5)
        t5.shift(DOWN*2.8 + RIGHT * 3.5)

        p1 = t1.get_bottom() + DOWN*0.2
        p2 = np.array((t1.get_bottom()[0], t2.get_left()[1], 0))
        p3 = t2.get_left()

        p4 = t2.get_right()
        p5 = np.array((t4.get_top()[0], t2.get_right()[1], 0))
        p6 = t4.get_top() + UP*0.2

        arrow1 = VGroup(
            Line(p1, p2, stroke_width=4),
            Arrow(p2, p3, buff=0, stroke_width=4)
        )
        arrow2 = VGroup(
            Line(p4, p5, stroke_width=4),
            Arrow(p5, p6, buff=0, stroke_width=4)
        )

        self.play(Write(t1))
        self.wait(12)
        self.play(FadeIn(arrow1))
        self.play(FadeIn(t2))
        self.wait(6)
        self.play(FadeIn(arrow2))
        self.play(Write(t4))
        self.wait(10)
        self.play(Create(bb1), Create(bb0))
        self.wait(2)
        self.add(rect)
        self.play(FadeOut(bb0, bb1, t2))
        self.wait(4)
        self.play(FadeIn(t3))
        self.remove(rect)
        self.wait(1)
        self.play(ReplacementTransform(t4, t5))

        bb2 = SurroundingRectangle(t1, color=RED, buff=SMALL_BUFF)
        bb3 = SurroundingRectangle(t5, color=RED, buff=SMALL_BUFF)

        self.wait()
        self.play(Create(bb2), Create(bb3))
        self.wait(2)
        self.play(FadeOut(bb2, bb3))
        self.wait(3)

        self.play(FadeOut(arrow1, arrow2, t1, t5))

        b1 = VGroup(
            MathTex(r"1\to 4"),
            MathTex(r"2\to 3"),
            MathTex(r"3\to 2"),
            MathTex(r"4\to 1"),
        ).arrange(DOWN, 0.4)
        b1.add(SurroundingRectangle(b1, color=WHITE, buff=MED_LARGE_BUFF))
        b1.next_to(t3, RIGHT, MED_SMALL_BUFF)

        b2 = VGroup(
            MathTex(r"1\to 1"),
            MathTex(r"2\to 2"),
            MathTex(r"3\to 3"),
            MathTex(r"4\to 4"),
        ).arrange(DOWN, 0.4)
        b2.add(SurroundingRectangle(b2, color=WHITE, buff=MED_LARGE_BUFF))
        b2.next_to(t3, LEFT, MED_SMALL_BUFF)

        dotdot1 = MathTex(r"...").scale(2).next_to(b1, RIGHT, buff=LARGE_BUFF, aligned_edge=RIGHT)
        dotdot2 = MathTex(r"...").scale(2).next_to(b2, LEFT, buff=LARGE_BUFF, aligned_edge=LEFT)

        t5 = MathTex(r"\text{Permutations of 4 elements } S_4").scale(1.3).shift(UP*3)
        self.wait()
        self.play(ReplacementTransform(t3, t2))
        self.play(FadeIn(b1))
        self.play(FadeIn(b2))
        self.play(Write(dotdot1), Write(dotdot2))
        self.wait(2)
        self.play(Write(t5))
        self.wait(6)
        symmetries = VGroup(b1, t2, b2, dotdot1)
        self.play(symmetries.animate.scale(0.5).shift(LEFT*1.5), FadeOut(dotdot2))
        b1 = Brace(symmetries, LEFT).scale(1.2)

        comp = MathTex(r"\circ").scale(2).next_to(symmetries, RIGHT, buff=LARGE_BUFF)

        comma = MathTex(r",").scale(2)
        comma.move_to((symmetries.get_right() + comp.get_left())/2)
        comma.shift(DOWN*0.3)

        b2 = Brace(symmetries, RIGHT).scale(1.2)
        b2.next_to(comp, RIGHT)
        self.play(FadeIn(b1, comma, comp, b2))
        self.wait(3)

class Scene7(Scene):
    def construct(self):
        self.wait(8)
        t1 = MathTex(r"\left( G, \circ \right) \Rightarrow", r"\text{symmetry?}").scale(1.2)
        t2 = MathTex(r"\left( \mathbb{R}, + \right) \Rightarrow", r"\text{symmetry?}").scale(1.2)
        t3 = MathTex(r"\left( \mathbb{R}, + \right) \Rightarrow", r"\text{(symmetry, composition)}").scale(1.2)
        t4 = MathTex(r"\Rightarrow ", r"\bigstar").scale(1.2)
        t4[1].become(Triangle().move_to(t4[1]).scale(0.7).shift(RIGHT*0.5))
        t4.next_to(t3, RIGHT, buff=-0.5)
        self.play(Write(t1))
        self.wait(6)
        self.play(ReplacementTransform(t1, t2))
        self.wait(12)
        self.play(ReplacementTransform(t2, t3))
        self.wait(12)
        self.play(t3.animate.shift(LEFT), FadeIn(t4))
        self.wait(8)

class Scene8(Scene):
    def construct(self):
        self.wait(3)
        t2 = MathTex(r"a\in \mathbb{R}").scale(1.4)
        t3 = MathTex(r"\left( \mathbb{R}, + \right)").scale(1.4)
        t4 = MathTex(r"t_a(x)=a+x").scale(1.4)
        t2.shift(LEFT*3.5)
        t3.shift(UP*1.5)
        t4.shift(RIGHT*3.5)
        a1 = Arrow(start=t2.get_right(), end=t4.get_left(), stroke_width=4, color=BLUE)
        a2 = Line(start=t3.get_bottom(), end=[t3.get_bottom()[0], a1.get_right()[1], 0], color=BLUE)
        t2.shift(LEFT*0.5)
        t3.shift(UP*0.5)
        t4.shift(RIGHT*0.5)
        total = VGroup(t2, t3, t4, a1, a2)
        total.move_to(ORIGIN)
        self.play(Write(t2))
        self.wait()
        self.play(Write(t3))
        self.play(FadeIn(a1, a2))
        self.wait(2)
        self.play(Write(t4))
        self.wait(7)
        t2n = MathTex(r"3\in \mathbb{R}").scale(1.4).move_to(t2)
        t4n = MathTex(r"t_3(x)=3+x").scale(1.4).move_to(t4)
        self.play(FadeOut(t2, t4))
        self.play(Write(t2n))
        self.play(Write(t4n))
        self.wait(5)
        self.play(FadeOut(t2n, t4n, a1, a2, t3))
        l1 = MathTex(r"t_3(x)=3+x").scale(1.4)
        l2 = MathTex(r"t_8(x)=8+x").scale(1.4)
        dotdot = MathTex(r"...")
        l3 = MathTex(r"t_5(x)=5+x").scale(1.4)
        composition = MathTex(r"\text{composition}").scale(1.5)
        comma = MathTex(r",").scale(2)
        ts = VGroup(l1, l2, dotdot, l3)
        ts.arrange(DOWN, 0.2)
        composition.next_to(ts, RIGHT, 1)
        b1 = Brace(ts, LEFT).scale(1.1)
        b2 = Brace(ts, RIGHT).scale(1.1)
        b2.next_to(composition, RIGHT)
        comma.move_to((ts.get_right() + composition.get_left())/2)
        comma.shift(DOWN*0.3)
        setoft = VGroup(b1, ts, comma, composition, b2)
        setoft.move_to(ORIGIN)
        symmetry = MathTex(r"\text{symmetries}").scale(1.5).move_to(ts)
        self.play(Write(l1))
        self.play(Write(l2))
        self.play(Write(dotdot), Write(l3))
        self.play(FadeIn(b1, b2, comma, composition))
        self.wait(5.5)
        self.play(ReplacementTransform(ts, symmetry), comma.animate.move_to(((symmetry.get_right() + composition.get_left())/2) + DOWN*0.3))
        self.wait(1)

class Scene9(Scene):
    def construct(self):
        self.wait(2)
        line = NumberLine(x_range=(-15, 15), include_numbers=True, color=BLUE).scale(1.2).shift(UP)
        shadow_line = line.copy().shift(DOWN*2).fade(0.5)
        zero_point = line.number_to_point(0)
        num_point = line.number_to_point(3)
        arrow = Arrow(zero_point, num_point, stroke_width=2, buff=0, color=GREEN)
        arrow.shift(MED_LARGE_BUFF*UP)
        self.play(Create(line), run_time=3)
        self.wait(1)
        self.play(line.animate.shift(0.5*RIGHT), run_time=1)
        self.play(line.animate.shift(1*LEFT), run_time=1)
        self.play(line.animate.shift(0.5*RIGHT), run_time=1)
        self.wait(2)
        self.play(FadeIn(shadow_line))
        t1 = MathTex(r"t_3(x)=3+x").scale(1.4).shift(UP*3)
        t2 = MathTex(r"t_2(x)=2+x").scale(1.4).shift(UP*3)
        t3 = MathTex(r"t_5(x)=5+x").scale(1.4).shift(UP*3)
        self.play(Create(arrow), FadeIn(t1))
        self.play(line.animate.shift(num_point - zero_point), run_time=2)
        self.play(FadeOut(arrow), FadeOut(t1))
        self.wait(4)
        arrow2 = Arrow(line.number_to_point(0), line.number_to_point(2), stroke_width=2, buff=0, color=GREEN)
        arrow2.shift(MED_LARGE_BUFF * UP)
        self.play(Create(arrow2), FadeIn(t2))
        self.play(line.animate.shift(line.number_to_point(2) - line.number_to_point(0)), run_time=2)
        self.play(FadeOut(arrow2), FadeOut(t2))
        self.wait()
        shadow_arrow = Arrow(shadow_line.number_to_point(0), shadow_line.number_to_point(5), stroke_width=2, buff=0, color=GREEN)
        shadow_arrow.shift(MED_LARGE_BUFF*UP)
        self.play(Create(shadow_arrow), FadeIn(t3))
        self.play(shadow_line.animate.shift(shadow_line.number_to_point(5) - shadow_line.number_to_point(0)), run_time=3)
        self.play(FadeOut(shadow_arrow), FadeOut(t3))
        self.wait(2)

class Scene10(Scene):
    def construct(self):
        self.wait()
        t3 = MathTex(r"\text{(symmetry, composition)} \Rightarrow ", r"\bigstar").scale(1.2)
        t3[1].become(Triangle().move_to(t3[1]).scale(0.7).shift(RIGHT*0.5))
        t3.shift(LEFT*0.5)
        self.play(Write(t3))
        self.wait(4)
        self.play(FadeOut(t3))
        self.wait()
        t4 = MathTex(r"\Big\{ \mathbb{R}, \mathcal{O}, \mathscr{A}, \text{frame field} \Big\}").scale(1.2)
        self.play(Write(t4))
        self.wait(16)
        line = NumberLine(x_range=(-15, 15))
        for x in range(-15, 14):
            current_num = x
            next_num = x + 1
            arrow = Arrow(line.number_to_point(current_num), line.number_to_point(next_num), stroke_width=2, buff=0, color=GREEN)
            arrow.shift(MED_LARGE_BUFF*UP)
            arrow.scale(0.9)
            line.add(arrow)
        shadow_line = line.copy().shift(DOWN*2).fade(0.5)
        self.play(t4.animate.shift(UP*2))
        self.play(FadeIn(line), run_time=1)
        self.play(FadeIn(shadow_line))
        self.wait(8)
        self.play(line.animate.shift(RIGHT), run_time=2)
        self.play(line.animate.shift(LEFT), run_time=2)
        self.wait()
        self.play(line.animate.scale(1.2), run_time=2)
        self.play(line.animate.scale(0.8333333333), run_time=2)
        self.wait()
        self.play(line.animate.rotate(180*DEGREES, UP, about_point=line.number_to_point(0)), run_time=2)
        self.play(line.animate.rotate(180*DEGREES, UP, about_point=line.number_to_point(0)), run_time=2)
        self.wait()

class Scene11(Scene):
    def construct(self):
        self.wait()
        t3 = MathTex(r"\text{(symmetry, composition)} \Rightarrow ", r"\bigstar").scale(1.2)
        t3[1].become(Triangle().move_to(t3[1]).scale(0.7).shift(RIGHT*0.5))
        t3.shift(LEFT*0.5)
        bb = SurroundingRectangle(t3, color=GREEN, buff=MED_SMALL_BUFF)
        self.play(Write(t3))
        self.play(Create(bb), run_time=2)
        self.play(Uncreate(bb), run_time=2)
        self.wait(4)
        self.play(FadeOut(t3, bb))
        self.wait(2)

        text = MathTex(r"\text{intuitive}", r"\Longleftrightarrow", r"\text{rigorous}").scale(1.5)
        self.play(Write(text))
        self.wait(4)
        self.play(Indicate(text[0]))
        self.play(Indicate(text[2]))
        self.wait(7)
        self.play(Indicate(text[2]))
        self.play(Indicate(text[0]))
        self.wait(8)
