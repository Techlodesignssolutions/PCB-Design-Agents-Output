from collections import defaultdict
from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

from skidl.pin import pin_types

SKIDL_lib_version = '0.0.1'

test_netlist = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'Conn_01x02', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'Conn_01x02'}), 'ref_prefix':'J', 'fplist':[''], 'footprint':'Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical', 'keywords':'connector', 'description':'Generic connector, single row, 01x02, script generated (kicad-library-utils/schlib/autogen/connector/)', 'datasheet':'~', 'pins':[
            Pin(num='1',name='Pin_1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='Pin_2',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'LED', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LED'}), 'ref_prefix':'D', 'fplist':[''], 'footprint':'LED_SMD:LED_0805_2012Metric', 'keywords':'LED diode', 'description':'Light emitting diode', 'datasheet':'~', 'pins':[
            Pin(num='1',name='K',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='A',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'R', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'R'}), 'ref_prefix':'R', 'fplist':[''], 'footprint':'Resistor_SMD:R_0805_2012Metric', 'keywords':'R res resistor', 'description':'Resistor', 'datasheet':'~', 'pins':[
            Pin(num='1',name='~',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='~',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] })])