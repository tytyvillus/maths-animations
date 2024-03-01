# manim -pql scene_functionised.py Scene1 
# ^ run command

from manim import *

global calc_scale
calc_scale = 0.9

class Scene1(Scene):
  def construct(self):
  # access global parameters 
    global numf, denomf, numg, denomg, denomh, \
      missing_facs_f, missing_facs_g, common_facs, \
      expanded_missing_facs_f, expanded_missing_facs_g, \
      new_numf, new_numg, numh, wait_times, colours
  
    # PARAMETERS for f + g = h 
    
    numf = (r"3x",)         # numerator of f, not bracketed, tuple
    denomf = (r"(2x-1)",)   # denominator of f, bracketed, tuple

    numg = (r"x-25",)       # numerator of g, not bracketed, tuple
    denomg = (r"(x-4)", r"(x+5)",) # denominator of g, bracketed, tuple
    
    # provide symbolic computations:
    
    # tuples:
    denomh = (*denomf, *denomg) # list of denom factors in h = f + g
    missing_facs_f = (*denomg,) # what f needs to be multiplied by
    missing_facs_g = (*denomf,) # what g needs to be multiplied by
    
    common_facs = 0 # int
    
    # strings:
    # first two by multiplying out missing_facs
    expanded_missing_facs_f = r"(x^2 + x - 20)" # bracketed, multiplicand for numf 
    expanded_missing_facs_g = r"(2x-1)" # bracketed, multiplicand for numg
    # next two by multiplying out num * expanded_missing_facs
    new_numf = r"3x^3 + 3x^2 - 60x"
    new_numg = r"2x^2 - 51x + 25"
    numh = r"3x^3 + 5x^2 - 111x + 25"
    
    wait_times = [ 
      4,  #  0. after writing "effectuer l'addition"
      4,  #  1. time before highlighting factors
      5,  #  2. time before moving factors into denominator of result
      8,  #  3. time before extracting first summand
      2,  #  4. time before multiplying first summand by 1
      4,  #  5. time before expanding 1 = missing_facs / missing_facs
      4,  #  6. time before beginning to work alongside
      2,  #  7. time before expanding the top right-hand bit
      2,  #  8. time before expanding the top (the rest)
      4,  #  9. time before focusing on second summand
      1,  # 10. time before multiplying first summand by 1
      1,  # 11. time before expanding 1 = missing_facs / missing_facs
      1,  # 12. time before beginning to work alongside
      0,  # 13. time before expanding the top right-hand bit
      1,  # 14. time before expanding the top (the rest)
      6,  # 15. time before summing new numerators
      2,  # 16. time between pickin up numf' and numg'
      2,  # 17. time to display summed numerator
      1,  # 18. time do wait before finalisin
      10, # 19. time to display boxed expr
      ]

    colours = [PURPLE, GOLD, MAROON, TEAL, BLUE, YELLOW, RED]
    # correct colouring relies on common factors b/n f and g being
    # respectively last (in f) and first (in g)
    
    # DO THE ~~THING~~ SCENE
    add_rationals(self)
  

class Scene2(Scene):
  def construct(self):
    # access global parameters 
    global numf, denomf, numg, denomg, denomh, \
      missing_facs_f, missing_facs_g, common_facs, \
      expanded_missing_facs_f, expanded_missing_facs_g, \
      new_numf, new_numg, numh, wait_times, colours
  
    # PARAMETERS for f + g = h 
    
    numf = (r"5",)         # numerator of f, not bracketed, tuple
    denomf = (r"(x+6)", r"(x-1)")   # denominator of f, bracketed, tuple

    numg = (r"2x",)       # numerator of g, not bracketed, tuple
    denomg = (r"(x-1)^2", r"(x+5)",) # denominator of g, bracketed, tuple
    
    # -> assumes common factors are adjacent, with greatest on the right
    # so that picks correct version when placing factors in denomh
    
    # provide symbolic computations:
    
    # tuples:
    denomh = (r"(x+6)", r"(x-1)^2", r"(x+5)",) # list of denom factors in h = f + g
    missing_facs_f = (r"(x-1)", r"(x+5)") # what f needs to be multiplied by
    missing_facs_g = (r"(x+6)",) # what g needs to be multiplied by
    
    common_facs = 1 # int
    
    # strings:
    # first two by multiplying out missing_facs
    expanded_missing_facs_f = r"(x^2 + 4x - 5)" # bracketed, multiplicand for numf 
    expanded_missing_facs_g = r"(x+6)" # bracketed, multiplicand for numg
    # next two by multiplying out num * expanded_missing_facs
    new_numf = r"5x^2 + 20x - 25"
    new_numg = r"2x^2 + 12x"
    numh = r"7x^2 + 32x - 25"
    
    wait_times = [ 
      10, #  0. after writing "effectuer l'addition"
      2,  #  1. time before highlighting factors
      3,  #  2. time before moving factors into denominator of result
      2,  #  3. time before extracting first summand
      2,  #  4. time before multiplying first summand by 1
      1,  #  5. time before expanding 1 = missing_facs / missing_facs
      2,  #  6. time before beginning to work alongside
      1,  #  7. time before expanding the top right-hand bit
      2,  #  8. time before expanding the top (the rest)
      4,  #  9. time before focusing on second summand
      1,  # 10. time before multiplying first summand by 1
      1,  # 11. time before expanding 1 = missing_facs / missing_facs
      1,  # 12. time before beginning to work alongside
      0,  # 13. time before expanding the top right-hand bit
      1,  # 14. time before expanding the top (the rest)
      4,  # 15. time before summing new numerators
      2,  # 16. time between pickin up numf' and numg'
      2,  # 17. time to display summed numerator
      1,  # 18. time do wait before finalisin
      10, # 19. time to display boxed expr
      ]

    colours = [PURPLE, GOLD, MAROON, TEAL, BLUE, YELLOW, RED]
    # correct colouring relies on common factors b/n f and g being
    # respectively last (in f) and first (in g)
    
    # DO THE ~~THING~~ SCENE
    add_rationals(self)
    
    
class Scene3(Scene):
  def construct(self):
    # access global parameters 
    global numf, denomf, numg, denomg, denomh, \
      missing_facs_f, missing_facs_g, common_facs, \
      expanded_missing_facs_f, expanded_missing_facs_g, \
      new_numf, new_numg, numh, wait_times, colours
  
    # PARAMETERS for f + g = h 
    
    numf = (r"x+5",)         # numerator of f, not bracketed, tuple
    denomf = (r"(x+6)", r"(x-1)^2")   # denominator of f, bracketed, tuple

    numg = (r"2x-1",)       # numerator of g, not bracketed, tuple
    denomg = (r"(x-1)^3", r"(x+5)",) # denominator of g, bracketed, tuple
    
    # provide symbolic computations:
    
    # tuples:
    denomh = (r"(x+6)", r"(x-1)^3", r"(x+5)",) # list of denom factors in h = f + g
    missing_facs_f = (r"(x-1)", r"(x+5)") # what f needs to be multiplied by
    missing_facs_g = (r"(x+6)",) # what g needs to be multiplied by
    
    common_facs = 1 # int
    
    # strings:
    # first two by multiplying out missing_facs
    expanded_missing_facs_f = r"(x^2 + 4x - 5)" # bracketed, multiplicand for numf 
    expanded_missing_facs_g = r"(x+6)" # bracketed, multiplicand for numg
    # next two by multiplying out num * expanded_missing_facs
    new_numf = r"x^3 + 9x^2 + 15x - 25"
    new_numg = r"2x^2 + 11x - 6"
    numh = r"x^3 + 11x^2 + 26x - 31"
    
    wait_times = [ 
      10, #  0. after writing "effectuer l'addition"
      2,  #  1. time before highlighting factors
      3,  #  2. time before moving factors into denominator of result
      2,  #  3. time before extracting first summand
      2,  #  4. time before multiplying first summand by 1
      1,  #  5. time before expanding 1 = missing_facs / missing_facs
      2,  #  6. time before beginning to work alongside
      3,  #  7. time before expanding the top right-hand bit
      3,  #  8. time before expanding the top (the rest)
      4,  #  9. time before focusing on second summand
      1,  # 10. time before multiplying first summand by 1
      1,  # 11. time before expanding 1 = missing_facs / missing_facs
      2,  # 12. time before beginning to work alongside
      0,  # 13. time before expanding the top right-hand bit
      4,  # 14. time before expanding the top (the rest)
      4,  # 15. time before summing new numerators
      2,  # 16. time between pickin up numf' and numg'
      2,  # 17. time to display summed numerator
      1,  # 18. time do wait before finalisin
      10, # 19. time to display boxed expr
      ]

    colours = [PURPLE, GOLD, MAROON, TEAL, BLUE, YELLOW, RED]
    # correct colouring relies on common factors b/n f and g being
    # respectively last (in f) and first (in g)
    
    # DO THE ~~THING~~ SCENE
    add_rationals(self)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# THE MEAT OF THE ANIMATION:

def add_rationals(self): 
  # needs global parameters to be defined before running

  # PARAMETERS for f + g = h 
  
  global numf     # numerator of f, not bracketed, tuple
  global denomf   # denominator of f, bracketed, tuple

  global numg     # numerator of g, not bracketed, tuple
  global denomg   # denominator of g, bracketed, tuple
  
  # tuples:
  global denomh   # list of denom factors in h = f + g
  global missing_facs_f   # what f needs to be multiplied by
  global missing_facs_g   # what g needs to be multiplied by
  
  global common_facs      # int
  
  # strings:
  # first two by multiplying out missing_facs
  global expanded_missing_facs_f  # bracketed, multiplicand for numf 
  global expanded_missing_facs_g  # bracketed, multiplicand for numg
  # next two by multiplying out num
  global new_numf 
  global new_numg 
  global numh 
  
  global wait_times # waiting times between actions

  global colours # colours to use for highlighting factors

  global calc_scale # how to scale the working expressions
  
  # PROBLEM STATEMENT

  # Text of main task
  task = Tex("Effectuer l'addition") # task for the algorithm
  main_expr = MathTex(
    r"{", *numf, r"\over", *denomf, "} + ",
    r"{", *numg, r"\over", *denomg, "}")
    
  # Find the indices for denums in above math_expr
  idx_df = 1 + len(numf) + 1            # where to start looking for denomf
  idx_dg = 1 + len(numf) + 1 + len(denomf) + 2 + len(numg) + 1 # -»- denomg
  
  # Initialise current colour to zero
  clr_idx = 0 
    
  # Arrange main text of task (with math_expr)
  VGroup(task, main_expr).arrange(DOWN, buff = 0.8)
  self.play(Write(task))
  self.play(Write(main_expr))
  self.wait(wait_times[0])
    
  # Clear the board, put math_expr top left
  self.play(Uncreate(task)) # remove text of task
  self.play(main_expr.animate(run_time=2).to_corner(UL)) # move top left
  self.wait(wait_times[1])
  
  # Highlight the factors in denums
  # factors in f
  for i in range(len(denomf)):
    self.play(
      Indicate(
        main_expr[idx_df + i],
        color = colours[clr_idx]
        )
      )
    main_expr[idx_df + i].set_color(colours[clr_idx])
    clr_idx += 1
  # colour common factors similarly by decrementing colour index
  clr_idx -= common_facs 
  # factors in g
  for i in range(len(denomg)):
    self.play(
      Indicate(
        main_expr[idx_dg + i].set_color(colours[clr_idx]),
        color = colours[clr_idx]
        )
      )
    clr_idx += 1
    
  self.wait(wait_times[2])
    
  # SET UP RESULT FRACTION
    
  # Start constructing the summed expr
  result_expr = MathTex(
    r"= { {{\quad}} \over" + 
    (len(denomh))*r"{{\quad}}" + # leaves spaces for exprs
    r"}")
  
  self.play(FadeIn(result_expr.next_to(main_expr, RIGHT)))
  
  # Add factors into the summed expr
  
  # start
  for i in range(len(denomh)):
  
    i += 1 # fix off-by-one errors
  
    # add them in
    new_result_expr = MathTex(
      r"= { {{ \quad \vphantom{x^2} }} \over ",
      *denomh[:i], # adds in expr
      (len(denomh)-i)*r"{{ \quad }}", # leaves spaces for exprs
      r"}"
      ).next_to(main_expr, RIGHT).shift(DOWN*.25) # hack for weird placement
      
    # colour them correctly
    for j in range(i): # set correct colours
      new_result_expr[3 + j].set_color(colours[j])
      
    # animate from main_expr:
    
    # first, compute correct index in main_expr
    if i < 1 + len(denomf) - common_facs:
      idx = idx_df + i - 1
    else:
      idx = idx_dg + i - (1 + len(denomf) - common_facs)
      
    # temporary expression for factor (x-x1)
    temp = main_expr.submobjects[idx].copy()
    
    # then, animate
    self.play(
      Transform(temp, result_expr.submobjects[2 + i]),
      Transform(result_expr, new_result_expr) # renew result_expr
      )
    self.remove(temp, new_result_expr)  
  # end
  
  self.wait(wait_times[3])
  
  # EXTRACT SUMMANDS AND MULTIPLY BY REMAINING FACTORS
    
  # For f
  
  f = main_expr[1 : idx_df + len(denomf)].copy().scale(calc_scale) # extract f
  self.play(f.animate.move_to(LEFT).to_edge(LEFT)) # animate f
  
  # multiply by 1
  frac_one = MathTex(r"\cdot\ 1").scale(calc_scale).next_to(f, RIGHT)
  
  self.wait(wait_times[4])
  self.play(FadeIn(frac_one))
  
  self.wait(wait_times[5])
  self.play( # expand 1 = missing_facs / missing_facs
    frac_one.animate.become(MathTex(
      r"\cdot\ {" + "".join([*missing_facs_f]) 
      + r"\over " + "".join([*missing_facs_f]) 
      + r"}"
      ).scale(calc_scale).next_to(f, RIGHT)
      )
    )
  self.wait(wait_times[6]) # time before beginning to work alongside
  
  # combine into one object 
  og_f = VGroup(f, frac_one)
  
  # work on it alongside (recolours bottom to white)
  working_f = MathTex(
    r"= { (" + "".join([*numf]) + r") \cdot" + "".join([*missing_facs_f])
    + r"\over" + "".join([*denomf]) + r"\cdot" + "".join([*missing_facs_f])
    + r"}").scale(calc_scale).next_to(og_f, RIGHT)
  self.play(ReplacementTransform(og_f.copy(), working_f))
  self.wait(wait_times[7])
    
  # expand out the top (right-hand bit)
  temp = MathTex(
    r" = { (" + "".join([*numf]) + ") \cdot" + expanded_missing_facs_f
    + r"\over" + "".join([*denomf]) + r"\cdot" + "".join([*missing_facs_f])
    + r"}").scale(calc_scale).next_to(og_f, RIGHT)
  self.play(FadeTransform(working_f, temp), run_time = 2)
  self.remove(temp)
  working_f = temp
  self.add(working_f)
  self.wait(wait_times[8])
  
  # expand out the top (the rest)
  ##temp = MathTex(
  ##  r"= {", new_numf,
  ##  r"\over " + "".join([*denomf]) + "".join([*missing_facs_f])
  ##  + r"}").next_to(og_f, RIGHT)
  temp = MathTex(
    r"= {", new_numf,
    r"\over " + "".join([*denomh]) + r"}").scale(calc_scale).next_to(og_f, RIGHT)
  self.play(FadeTransform(working_f, temp), run_time = 2)
  self.remove(temp)
  working_f = temp
  self.add(working_f)
  self.wait(wait_times[9])

  # For g
  
  g = main_expr[idx_dg - len(numg) - 1:].copy() # extract g
  self.play(g.animate.to_corner(DL)) # animate g
  
  # multiply by 1
  frac_one = MathTex(r"\cdot\ 1").scale(calc_scale).next_to(g, RIGHT)
  
  self.wait(wait_times[10])
  self.play(FadeIn(frac_one))
  
  self.wait(wait_times[11])
  self.play( # expand 1 = missing_facs / missing_facs
    frac_one.animate.become(MathTex(
      r"\cdot\ {" + "".join([*missing_facs_g]) 
      + r"\over " + "".join([*missing_facs_g]) 
      + r"}"
      ).scale(calc_scale).next_to(g, RIGHT)
      )
    )
  self.wait(wait_times[12])
  
  # combine into one object 
  og_g = VGroup(g, frac_one)
  
  # work on it alongside (recolours bottom to white)
  temp = r" = { (" + "".join([*numg]) + r") \cdot" + "".join([*missing_facs_g]) \
    + r"\over" + "".join([*denomg]) + r"\cdot" + "".join([*missing_facs_g]) + r"}"
  working_g = MathTex(temp).next_to(og_g, RIGHT).scale(calc_scale)
  self.play(ReplacementTransform(og_g.copy(), working_g))
  self.wait(wait_times[13])
    
  # expand out the top (right-hand bit)
  temp = MathTex(
    r" = { (" + "".join([*numg]) + r") \cdot" + expanded_missing_facs_g
    + r"\over" + "".join([*denomg]) + r"\cdot" + "".join([*missing_facs_g])
    + r"}").scale(calc_scale).next_to(og_g, RIGHT)
  self.play(FadeTransform(working_g, temp), run_time = 2)
  self.remove(temp)
  working_g = temp
  self.add(working_g)
  self.wait(wait_times[14])
  
  # expand out the top (the rest)
  temp = MathTex(
    r"= {", new_numg,
    r"\over " + "".join([*denomg]) + "".join([*missing_facs_g])
    + r"}").scale(calc_scale).next_to(og_g, RIGHT)
  self.play(FadeTransform(working_g, temp), run_time = 2)
  self.remove(temp)
  working_g = temp
  self.add(working_g)
  self.wait(wait_times[15])

  # SUM SUMMANDS TO GET NUMERATOR OF h

  result_num_summand_f = working_f[1].copy().scale(1/calc_scale).move_to(UP)
  result_num_summand_g = working_g[1].copy().scale(1/calc_scale).move_to(DOWN)
  plus = MathTex("+")
  
  numh_mobject = MathTex(numh)
  
  # pick up contribution from f
  self.play(
    FadeOut(og_f, working_f),
    ReplacementTransform(working_f[1].copy(), result_num_summand_f)
    ) 
    
  # plus
  self.play(FadeIn(plus))
  
  # pick up contribution from g
  self.play(
    FadeOut(og_g, working_g),
    ReplacementTransform(working_g[1].copy(), result_num_summand_g)
    ) 
   
  self.wait(wait_times[16])
    
  # compute the sum
  self.play(ReplacementTransform(
    VGroup(result_num_summand_f, plus, result_num_summand_g),
    numh_mobject))
    
  self.wait(wait_times[17])
  
  # MOVE RESULT INTO NUM h, COMPLETING IT
  
  # recreate num h
  new_result_expr = MathTex(
    r"= {", numh, r"\over ",
    *denomh[:len(denomh)], # adds in expr
    r"}"
    ).next_to(main_expr, RIGHT)       
  # and set correct colours
  for j in range(len(denomh)): 
    new_result_expr[3 + j].set_color(colours[j])
    
  # move numerator into h
  self.play(Transform(numh_mobject, new_result_expr[1]))
  self.wait(wait_times[18])
  
  # MOVE INTO CENTER STAGE
  
  full_expr = VGroup(main_expr, new_result_expr)
  
  #self.play(FadeTransform(result_expr, new_result_expr))
  self.remove(numh_mobject, result_expr)
  
  self.play(full_expr.animate.move_to(ORIGIN))
  self.play(Create(
    SurroundingRectangle(full_expr, buff = .3, color=colours[clr_idx])
    ))
    
  self.wait(wait_times[19])
