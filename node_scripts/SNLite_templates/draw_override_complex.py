"""
in floats_in s .=[] n=0.0
out floats_out s
draw curve_draw
ui = my_temp_material, RGB Curves
"""

import bpy

from sverchok.utils.snlite_utils import get_valid_evaluate_function as get_evaluator

evaluate = get_evaluator('my_temp_material', 'RGB Curves')

def curve_draw(self, context, layout):
    m = bpy.data.materials.get('my_temp_material')
    if not m:
        return
    tnode = m.node_tree.nodes['RGB Curves']
    layout.template_curve_mapping(tnode, "mapping", type="NONE")


floats_out = []
for flist in floats_in:
    floats_out.append([evaluate(v) for v in flist])