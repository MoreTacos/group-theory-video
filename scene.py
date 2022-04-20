from manim import *

class Scene1(Scene):
    def construct(self):
        # part 1
        self.wait(2)
        t1 = Text("Group Theory")
        t1.scale(2)
        self.play(Write(t1))
        self.wait(1)
        self.play(t1.animate.shift(UP*3).scale(0.7))
        self.wait(1)
        
        # part 2
        t2 = MathTex(r"\left( G, \circ  \right)")
        t3 = Text("Associative")
        t4 = Text("Neutral Element")
        t5 = Text("Inverses")
        t2.shift(LEFT*4).scale(2)
        t3.next_to(t2, DOWN)
        t3.scale(0.6)
        t4.next_to(t3, DOWN)
        t4.scale(0.6)
        t5.next_to(t4, DOWN)
        t5.scale(0.6)
        self.play(Write(t2), Write(t3), Write(t4), Write(t5))
        self.wait(2)

        # part 3
        t6 = Text("Symmetry")
        triangle = Triangle()
        t6.shift(RIGHT*4)
        t6.shift(DOWN*2.5)
        t6.scale(0.7)
        triangle.shift(RIGHT*4)
        triangle.shift(DOWN*0.6)
        triangle.scale(1.8)
        sym1 = DashedLine(triangle.get_vertices()[0], (triangle.get_vertices()[1] + triangle.get_vertices()[2])/2)
        sym2 = DashedLine(triangle.get_vertices()[1], (triangle.get_vertices()[2] + triangle.get_vertices()[0])/2)
        sym3 = DashedLine(triangle.get_vertices()[2], (triangle.get_vertices()[0] + triangle.get_vertices()[1])/2)
        sym1.scale(1.3)
        sym2.scale(1.3)
        sym3.scale(1.3)
        self.play(FadeIn(triangle), Write(t6))
        self.play(FadeIn(sym1), FadeIn(sym2), FadeIn(sym3))
        self.wait(1)
        a1 = MathTex(r"\Leftrightarrow")
        q1 = Text("?")
        a1.scale(2.5)
        q1.scale(1.6)
        a1.shift(DOWN)
        self.play(Write(a1), Write(q1))
        self.wait(2)

class Scene2(Scene):
    def construct(self):
        self.wait(2)
        t1 = MathTex(r"\text{intuitive} \Rightarrow \text{rigorous}")
        t1.scale(2)
        self.play(Write(t1))
        self.wait(2)
        self.play(FadeOut(t1))
        # ---
        triangle = Triangle()
        triangle.scale(2)
        triangle.shift(LEFT*3.5)
        ts1 = MathTex(r"\to \text{top flip}")
        ts2 = MathTex(r"\to \text{left flip}")
        ts3 = MathTex(r"\to \text{right flip}")
        ts1.shift(UP*0.5)
        ts3.shift(DOWN*0.5)
        self.play(FadeIn(triangle))
        self.wait(1)
        self.play(Write(ts1), triangle.animate.flip(UP))
        self.wait(1)
        self.play(Write(ts2), triangle.animate.flip(DOWN + LEFT*1.732051, about_point=triangle.get_center_of_mass()))
        self.wait(1)
        self.play(Write(ts3), triangle.animate.flip(DOWN + RIGHT*1.732051, about_point=triangle.get_center_of_mass()))
        self.wait(2)
        # ---
        ts4 = MathTex(r'\to \text{rotate 120}')
        ts4.shift(UP*0.5 + RIGHT*3)

        ts5 = MathTex(r"\to \text{rotate -120}")
        ts5.shift(RIGHT*3)

        ts6 = MathTex(r"\to \text{do nothing}")
        ts6.shift(DOWN*0.5 + RIGHT*3)
        self.play(Write(ts4), triangle.animate.rotate(-120*DEGREES, about_point=triangle.get_center_of_mass()))
        self.wait(1)

        self.play(Write(ts5), triangle.animate.rotate(120*DEGREES, about_point=triangle.get_center_of_mass()))
        self.wait(2)

        self.play(Write(ts6), triangle.animate.rotate(0*DEGREES, about_point=triangle.get_center_of_mass()))
        self.wait(1)
        sy1 = Text("Symmetry?")
        sy1.scale(1.2)
        sy1.shift(UP*2)
        self.play(ts1.animate.shift(DOWN),
                  ts2.animate.shift(DOWN),
                  ts3.animate.shift(DOWN),
                  ts4.animate.shift(DOWN),
                  ts5.animate.shift(DOWN),
                  ts6.animate.shift(DOWN),
                  triangle.animate.shift(DOWN),
                  Write(sy1))
        self.wait(2)

class Scene3(Scene):
    def construct(self):
        # part 1
        self.wait(2)
        t1 = Text("duality")
        t1.scale(2)
        self.play(Write(t1))
        self.wait(3)



class Scene4(Scene):
    def construct(self):
        # part 1
        self.wait(2)
        t1 = Text("adjective")
        t2 = Text("verb")
        t1.scale(1.2)
        t2.scale(1.2)
        t1.shift(UP * 1.8 + LEFT * 3)
        t2.shift(UP * 1.8 + RIGHT * 3)


        triangle = Triangle()
        t3 = Text(r'"That triangle is very symmetric"')
        t3.shift(LEFT*3 + DOWN*3)
        t3.scale(0.5)
        
        triangle.shift(LEFT*3)
        triangle.shift(DOWN)
        triangle.scale(1.8)
        sym1 = DashedLine(triangle.get_vertices()[0], (triangle.get_vertices()[1] + triangle.get_vertices()[2])/2)
        sym2 = DashedLine(triangle.get_vertices()[1], (triangle.get_vertices()[2] + triangle.get_vertices()[0])/2)
        sym3 = DashedLine(triangle.get_vertices()[2], (triangle.get_vertices()[0] + triangle.get_vertices()[1])/2)
        sym1.scale(1.3)
        sym2.scale(1.3)
        sym3.scale(1.3)

        self.play(Write(t1), FadeIn(triangle))
        self.wait(1)
        self.play(FadeIn(sym1), FadeIn(sym2), FadeIn(sym3), Write(t3))
        self.wait(3)
        vg = VGroup()
        h1 = Text(r"flip_top(x)")
        h2 = Text(r"flip_right(x)")
        h3 = Text(r"flip_left(x)")
        h4 = Text(r"rotate_120(x)")
        h5 = Text(r"rotate_240(x)")
        h6 = Text(r"do_nothing(x)")
        h2.next_to(h1, DOWN)
        h3.next_to(h2, DOWN)
        h4.next_to(h3, DOWN)
        h5.next_to(h4, DOWN)
        h6.next_to(h5, DOWN)
        vg.add(h1)
        vg.add(h2)
        vg.add(h3)
        vg.add(h4)
        vg.add(h5)
        vg.add(h6)
        vg.shift(RIGHT*3 + UP)
        vg.scale(0.7)
        b1 = Brace(vg, direction=LEFT)
        b2 = Brace(vg, direction=RIGHT)

        self.play(Write(t2), FadeIn(vg), FadeIn(b1), FadeIn(b2))
        self.wait(2)

        j1 = Text("Instrinsic Symmetries")
        j2 = MathTex(r"\Rightarrow")
        j3 = Text("Set of Symmetries")
        j1.shift(UP*1.5)
        j2.scale(3)
        j3.shift(DOWN*1.5)

        jtotal = VGroup()
        jtotal.add(j1)
        jtotal.add(j2)
        jtotal.add(j3)
        self.play(vg.animate.shift(RIGHT*2.5), t2.animate.shift(RIGHT*2.5), b1.animate.shift(RIGHT*2.5), b2.animate.shift(RIGHT*2.5),
                  triangle.animate.shift(LEFT*2.5), sym1.animate.shift(LEFT*2.5), sym2.animate.shift(LEFT*2.5), sym3.animate.shift(LEFT*2.5), t1.animate.shift(LEFT*2.5), t3.animate.shift(LEFT*2.5))
        self.play(Write(jtotal))
        self.wait(2)

class TriangleGroup(RegularPolygon):
    def __init__(self, **kwargs):
        super().__init__(n=3, **kwargs)
    def with_top(self):
        sym = DashedLine(self.get_bottom(), self.get_top())
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
        vertex = np.array((self.get_right()[0], self.get_bottom()[1], 0.0))
        midpoint = np.array(((self.get_left()[0] + self.get_top()[0])/2, (self.get_bottom()[1] + self.get_top()[1])/2, 0.0))
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
        vertex = np.array((self.get_left()[0], self.get_bottom()[1], 0.0))
        midpoint = np.array(((self.get_right()[0] + self.get_top()[0])/2, (self.get_bottom()[1] + self.get_top()[1])/2, 0.0))
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
        radius = self.get_top()[1] - self.get_center_of_mass()[1]
        arrow = Arc(radius*1.3, start_angle=90 * DEGREES, angle=-DEGREES*120, num_components=9, arc_center=self.get_center_of_mass())
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
        radius = self.get_top()[1] - self.get_center_of_mass()[1]
        arrow = Arc(radius*1.3, start_angle=90 * DEGREES, angle=DEGREES*120, num_components=9, arc_center=self.get_center_of_mass())
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
        # part 1
        self.wait(2)
        vg = VGroup()
        h1 = Text(r"flip_top(x)")
        h5 = Text(r"flip_right(x)")
        h3 = Text(r"flip_left(x)")
        h4 = Text(r"rotate_120(x)")
        h2 = Text(r"rotate_240(x)")
        h6 = Text(r"do_nothing(x)")
        h2.next_to(h1, RIGHT * 4)
        h3.next_to(h2, RIGHT * 4)
        h4.next_to(h1, DOWN)
        h5.next_to(h2, DOWN)
        h6.next_to(h3, DOWN)
        vg.add(h1)
        vg.add(h2)
        vg.add(h3)
        vg.add(h4)
        vg.add(h5)
        vg.add(h6)
        vg.scale(0.6)
        b1 = Brace(vg, direction=LEFT)
        b2 = Brace(vg, direction=RIGHT)
        vg.add(b1)
        vg.add(b2)
        vg.next_to(UP, UP)
        self.play(Write(vg))
        self.wait(2)

        t1 = Text("Group?")
        t2 = Text("Composition")
        t1.scale(1.5)
        t1.shift(DOWN)
        t2.scale(1.5)
        t2.shift(DOWN)
        self.play(Write(t1))
        self.wait(2)
        self.play(ReplacementTransform(t1, t2))
        self.wait(2)
        self.play(FadeOut(t2))
        self.wait(1)

        # part 2

        tr1 = TriangleGroup()
        comp1 = MathTex(r"\circ")
        tr2 = TriangleGroup()
        equal1 = MathTex(r"=")
        tr3 = TriangleGroup()

        line1 = VGroup(tr1, comp1, tr2, equal1, tr3)
        line1.arrange(RIGHT, 1)
        line1.move_to(ORIGIN)
        line1.shift(DOWN)

        self.play(Create(line1), run_time=2)
        self.wait(1)
        self.play(tr1.rotate120(), Indicate(h4))
        self.play(tr2.rotate240(), Indicate(h2))
        self.play(tr3.do_nothing(), Indicate(h6))
        self.wait(1)
        self.play(tr1.flip_top(), Indicate(h1))
        self.play(tr2.flip_right(), Indicate(h5))
        self.play(tr3.rotate120(), Indicate(h4))
        self.wait(2)

class Scene6(Scene):
    def construct(self):
        # part 1
        self.wait(2)
        t1 = Text(r"(symmetries, composition) is a group")
        t1.move_to(UP*2)
        self.play(Write(t1))
        self.wait(1)
        t21 = Text("1.")
        t2 = MathTex(r"\left( a\circ b \right)\circ c = a \circ \left( b\circ c \right)")
        t2 = VGroup(t21, t2)
        t2.arrange(RIGHT, 0.5)
        self.play(Write(t2))

        tr1 = TriangleGroup().with_right()
        comp1 = MathTex(r"\circ")
        tr2 = TriangleGroup().with_rotate240()
        equal1 = MathTex(r"=")
        tr3 = TriangleGroup().with_top()

        line1 = VGroup(tr1, comp1, tr2, equal1, tr3)
        line1.arrange(RIGHT, 1)
        line1.move_to(ORIGIN)
        self.play(FadeIn(line1))
        self.wait(2)
