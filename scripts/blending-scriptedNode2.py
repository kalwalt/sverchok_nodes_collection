#some experiments wiyh SvScriptedNode2 and blending functions
class Blending(SvScriptAuto): 
    @staticmethod
    def function(*args):
        
        base = args[0]
        blend = args[1]
        blend_types = args[2]
        out = []
        if blend_types == 0:
            
            out = base+blend
            print('addiction: '+str(out))
        elif blend_types == 1:
            
            out = base * blend
            print('multiplication: ' + str(out))
        
        elif blend_types == 2:
        #division
            out = base / blend
        
            print('division: ' + str(out))
        
        elif blend_types == 3: 
        #screen
            out = 1-(1-base)*(1-blend)
            
            print('screen:' + str(out))
            
        elif blend_types == 4:
        #overlay   
            if base < 0.5:
                
                out = 2*base*blend
                
            else:
                out = 1-2*(1-base)*(1-blend)
            print('overlay:' + str(out)) 
        
        return out
    
    name = "Blending function"

    inputs = [("s", "Base", 0),
             ("s", "Blend", 0),
             ("s","Blend_types",0)]
    outputs = [("s", "Res")]