# Randomness

![sine(x)](../../images/tutorial_noise_sverchok/sin(x).png)

We start with a simple sine function, and we will continue  adding more and more complexity.
In Sverchok is pretty simple just few nodes and you can display a sine function.

![sine sverchok](../../images/tutorial_noise_sverchok/sine_sv.png)

We can achieve randomness, modulating, distorting and increasing the frequency and amplitude of the sinusoidal curve. In sinthesis adding a
kind of disorder to this ordered shape. But let's make a step in between the full randomness. What's happens if we plug the sine function into a fractional?

![fractional_sine](../../images/tutorial_noise_sverchok/fract_sin(x).png)

We obtain a curve with pikes and vertical jumps, but still quite ordered. How we can get
this in Sverchok? This is yet quite simple see the picture below:

![fractional_sine_sv](../../images/tutorial_noise_sverchok/fractional_sin_function.png)

In Sverchok we use the modulo function from the `Math node` in order to achieve
the fractional(Glsl) that is a sawtooth curve:

![fractional](../../images/tutorial_noise_sverchok/fractional.png)

![fractional_sv](../../images/tutorial_noise_sverchok/fractional_sv.png)

As said before we modulate the curve to obtain more chaos. Try to multiply
the amplitude with a 10000 factor. Suddenly the ordered shape lose is clarity
and emphasis.

![fractional_sine_x_10000_sv](../../images/tutorial_noise_sverchok/fractional_sin_function_X_10000.png)

We can go further in this direction, let's add to this function more 'noise'.
Let's take the **x** and **y** vector component of the line and we perform a dot product
with `x = 12.9898` and `y = 78.233`
before the sinusoidal function, and we increase the amplitude to a considerable value, let's say to `43758.5453123`.
Finally we can observ a random curve:

![random_function_sv](../../images/tutorial_noise_sverchok/fractional_sin_random_function.png)

In the next chapter we will develop this tree nodes in something more visually interesting.
We will talk about noise.
