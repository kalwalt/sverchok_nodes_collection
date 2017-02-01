# sverchok_nodes_collection
Various nodes and blend files for the sverchok blender addon.

* Polyvox experiments with sverchok addon. For now only some tests: you can find .blend, .json, and .py template to use with sv_ScriptedNode. Included PolyVoxCore.py and _PolyVoxCore.so for linux64.
  * polyvox_Cubic_simple_test.py : the basic examples with the cubic extractor.
  * polyvox_Cubic_simple_test.py : the basic examples with the Marching cubes extractor.
  * polyvox-terrain.py : a simple terrain example with  fractal blender noise
  * polyvox_sphere_noise_test.py : a distance field with a noise modulation.

* Fractals scripts using the 'mathutils.noise' blender functions
  * fbm.py : fractal brownian motion implementation for various uses.
  * blending-scriptedNode2.py : some blending fuctionality in one script: addition,multiplication,division, screen, overlay.
  * turbulence.py : turbulence function, return float.

**Arch**: only linux64 for now.

Polyvox is a C++ library for voxel creation. Go here for a description: http://www.volumesoffun.com/polyvox-documentation/



#### Todo

* more examples and other .json utilites, some little tutorials on basic mesh prototiping.
* extending the polyvox scripting nodes in order to have practical tools for voxelizing. (and maybe become part of the sverchok addon itself).
* Polyvox python bindings for windows.
* Upgrade the Polyvox bindings to the latest in dev.
