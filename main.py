from functions import *

parser = argparse.ArgumentParser(description='Command line client for generating geometries')
parser.add_argument('-n1', '--number1', dest="number1", default=math.pi, required=False, help="Number 1")
parser.add_argument('-n2', '--number2', dest="number2", required=False, help="Number 2")
parser.add_argument('-n3', '--number3', dest="number3", required=False, help="Number 3")
parser.add_argument('-ref', '--ref', default="1", dest="reference", help="Number Reference")
args = parser.parse_args()

#input parsing
n1 = args.number1
ref = args.reference

print(n1)
print(ref)

dpg.create_context()
dpg.create_viewport(title='Rafiki', width=window_width, height=window_height)
dpg.set_viewport_vsync(True) #False will run fast as possible
dpg.setup_dearpygui()


with dpg.window(label="Main Window", tag="Primary_Window", width=window_width, height=window_height):
    dpg.add_checkbox(label="show moon", callback=toggle_layer1, default_value=True, pos=[window_width - 150, 0])
    #dpg.add_button(label="Take Shot", callback=screenShot)
    with dpg.drawlist(width=window_width, height=window_height):
            with dpg.draw_node(tag="root node"):
                dpg.draw_circle([0, 0], 3, color=[255, 223, 0, 150], fill=[255, 223, 0, 150]) # sun/center
                dpg.draw_text((0, -6), "Origin", color=(250, 250, 250, 255), size=10)
                
                with dpg.draw_node(tag="node 1", label="n1_line"):
                    dpg.draw_line((0, 0), (planet1_distance, 0), color=(255, 0, 0, 255), thickness=1)

                    with dpg.draw_node(tag="planet node 1", label="planet1"):
                        dpg.draw_circle(planet1_pos, 10, color=[0, 255, 0], fill=[0, 255, 0]) # inner planet
                        dpg.draw_circle(planet1_pos, 25, color=[255, 255, 0], tag="moon1 orbit")                 # moon orbit path

                        with dpg.draw_node(tag="planet 1, moon node"):
                            dpg.draw_circle(planet1_moon1_pos, 5, color=[255, 255, 0], fill=[255, 255, 0]) # moon



with dpg.window(label="Example Window 2"):
    dpg.add_text("Hello, world2")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

#initial conditions
dpg.apply_transform("root node", dpg.create_translation_matrix([root_x, root_y]))
dpg.apply_transform("planet node 1", dpg.create_rotation_matrix(math.pi*planet1_angle/180.0 , [0, 0, -1])*dpg.create_translation_matrix([planet1_distance, 0]))
dpg.apply_transform("planet 1, moon node", dpg.create_rotation_matrix(math.pi*planet1_moon1angle/180.0 , [0, 0, -1])*dpg.create_translation_matrix([planet1_moon1distance, 0]))

dpg.show_viewport()
dpg.set_primary_window("Primary_Window", True)

while dpg.is_dearpygui_running():

    a = stepAngles()
    
    dpg.apply_transform("node 1", dpg.create_rotation_matrix(math.pi*a['p1']/180.0 , [0, 0, -1]))
    dpg.apply_transform("planet node 1", dpg.create_translation_matrix([planet1_distance, 0]))
    dpg.apply_transform("planet 1, moon node", dpg.create_rotation_matrix(math.pi*a['m1']/180.0 , [0, 0, -1])*dpg.create_translation_matrix([planet1_moon1distance, 0]))

    dpg.render_dearpygui_frame()
    
dpg.destroy_context()