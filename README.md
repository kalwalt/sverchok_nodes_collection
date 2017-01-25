# sverchok_nodes_collection
Various nodes and blend files for the sverchok blender addon.

* Polyvox experiments with sverchok addon. For now only some tests: you can find .blend, .json, and .py template to use with sv_ScriptedNode. Included PolyVoxCore.py and _PolyVoxCore.so for linux64.
  * polyox-test.py : the basic examples
  * polyvox-terrain.py : a simple terrain example with  fractal blender noise

* Fractals scripts using the 'mathutils.noise' blender functions
  * fbm.py : fractal brownian motion implementation for various uses.

**Arch**: only linux64 for now.



#### Todo

* more examples and other .json utilites, some little tutorials on basic mesh prototiping.
* extending the polyvox scripting nodes in order to have practical tools for voxelizing. (and maybe become part of the sverchok addon itself).
* Polyvox python bindings for windows.
* Upgrade the Polyvox bindings to the latest in dev.
