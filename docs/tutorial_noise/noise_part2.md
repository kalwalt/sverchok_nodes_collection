# Noise

We start from the last series of nodes. We are arrived to make a random curve. Probably you know that doesn't exist truly randomness, we not go deeper this aspect too far because goes beyond our goals. we just note that there are different implementations, if you want goes at the end of the tutorial you will find some information source. Let's back instead to Sverchok nodes, this was the last:

![random nodes](../../images/tutorial_noise_sverchok/fractional_sin_random_function.png)

Interpreted as an image can be something like this:

![radnomness](../../images/tutorial_noise_sverchok/randomness.png)

this is also called "white noise", something that is omogeneous and pretty boring
from a visual aspect. We have to go a step further. In the 80es Ken Perlin developed
his well known Perlin algorithm for the film Thron. We do not recreate the same algorithm, but something closer to it.
We will approach to it taking small steps. The first, is to transform the random function above, expressed by a irregular curve in a stepped one. with an only node: just connect a floor from a
`Math` node between the **x** vector component, see the image below:

![random_plus_floor](../../images/tutorial_noise_sverchok/fractional_sin_random_function_plus_floor.png)

Well, you will say: What deal this with the randomness? This is an important step: We modulate that function in something less dramatic, adding more complexity. we create a second branch from the **x** Vector component with a more node, a `Math` add node, the result of the two branch and another x modulo is the modulo factor for the mix function of the two branch. Take a look at the picture:

![mix_norm](../../images/tutorial_noise_sverchok/fractional_sin_random_function_mix_norm.png)

as a final step we add a smoothstep function and we will get a 1 dimensional Noise:

![Noise_1D](../../images/tutorial_noise_sverchok/noise 1D.png)

Surprisingly we have a curve that looks like the profile of a mountain and a natural landscape. But we started instead from a chaotic shape... this is one of the most interesting and fascinating aspects of noise creation.
