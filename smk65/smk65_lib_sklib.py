from skidl import Pin, Part, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

smk65fox_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(name='MX_LED',dest=TEMPLATE,tool=SKIDL,d_ref='D1',d_pin=5,col=1,row=1,ref_prefix='M',num_units=2,fplist=['cherry'],do_erc=True,footprint='Keyboard:MXALPS',pins=[
            Pin(num='SW1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='SW2',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='A',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='K',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='1SS309',dest=TEMPLATE,tool=SKIDL,keywords='diode',description='1SS309 Quad Switching Diode Common Cathode',row=1,ref_prefix='D',num_units=4,fplist=['Housings_SOT-25-5', 'SC-74A'],do_erc=True,footprint='Keyboard:SC-74A',pins=[
            Pin(num='1',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='A',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='K',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='A',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='ATmega32U4-AU',dest=TEMPLATE,tool=SKIDL,keywords='AVR 8bit Microcontroller MegaAVR USB',description='TQFP44, 32K Flash, 2.5K SRAM, 1K EEPROM, USB2.0',ref_prefix='U',num_units=1,do_erc=True,footprint='Housings_QFP:TQFP-44_10x10mm_Pitch0.8mm',pins=[
            Pin(num='1',name='(INT6/AIN0)PE6',do_erc=True),
            Pin(num='2',name='UVCC',do_erc=True),
            Pin(num='3',name='D-',do_erc=True),
            Pin(num='4',name='D+',do_erc=True),
            Pin(num='5',name='UGND',do_erc=True),
            Pin(num='6',name='UCAP',do_erc=True),
            Pin(num='7',name='VBUS',do_erc=True),
            Pin(num='8',name='(SS/PCINT0)PB0',do_erc=True),
            Pin(num='9',name='(SCLK/PCINT1)PB1',do_erc=True),
            Pin(num='10',name='(PDI/MOSI/PCINT2)PB2',do_erc=True),
            Pin(num='20',name='(RXD/INT2)PD2',do_erc=True),
            Pin(num='30',name='(ADC13/OC1B/OC4B/PCINT13)PB6',do_erc=True),
            Pin(num='40',name='(ADC1)PF1',do_erc=True),
            Pin(num='11',name='(PDO/MISO/PCINT3)PB3',do_erc=True),
            Pin(num='21',name='(TXD/INT3)PD3',do_erc=True),
            Pin(num='31',name='(OC3A/~OC4A~)PC6',do_erc=True),
            Pin(num='41',name='(ADC0)PF0',do_erc=True),
            Pin(num='12',name='(OC0A/OC1C/~RTS~/PCINT7)PB7',do_erc=True),
            Pin(num='22',name='(XCK1/~CTS~)PD5',do_erc=True),
            Pin(num='32',name='(ICP3/CLK0/OC4A)PC7',do_erc=True),
            Pin(num='42',name='AREF',do_erc=True),
            Pin(num='13',name='RESET',do_erc=True),
            Pin(num='23',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='33',name='(~HWB~)PE2',do_erc=True),
            Pin(num='43',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='14',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='24',name='AVCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='34',name='VCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='44',name='AVCC',func=Pin.PWRIN,do_erc=True),
            Pin(num='15',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='25',name='(ICP2/ADC8)PD4',do_erc=True),
            Pin(num='35',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='16',name='XTAL2',do_erc=True),
            Pin(num='26',name='(T1/~OC4D~/ADC9)PD6',do_erc=True),
            Pin(num='36',name='(ADC7/TDI)PF7',do_erc=True),
            Pin(num='17',name='XTAL1',do_erc=True),
            Pin(num='27',name='(T0/OC4D/ADC10)PD7',do_erc=True),
            Pin(num='37',name='(ADC6/TDO)PF6',do_erc=True),
            Pin(num='18',name='(OC0B/SCL/INT0)PD0',do_erc=True),
            Pin(num='28',name='(ADC11/PCINT4)PB4',do_erc=True),
            Pin(num='38',name='(ADC5/TMS)PF5',do_erc=True),
            Pin(num='19',name='(SDA/INT1)PD1',do_erc=True),
            Pin(num='29',name='(ADC12/OC1A/~OC4B~/PCINT12)PB5',do_erc=True),
            Pin(num='39',name='(ADC4/TCK)PF4',do_erc=True)]),
        Part(name='C',dest=TEMPLATE,tool=SKIDL,keywords='cap capacitor',description='Unpolarized capacitor',ref_prefix='C',num_units=1,fplist=['C_*'],do_erc=True,footprint='Capacitors_SMD:C_0805',pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='R',dest=TEMPLATE,tool=SKIDL,keywords='r res resistor',description='Resistor',ref_prefix='R',num_units=1,fplist=['R_*', 'R_*'],do_erc=True,footprint='Resistors_SMD:R_0805',pins=[
            Pin(num='1',name='~',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='~',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='FP_Small',dest=TEMPLATE,tool=SKIDL,description='Fuse polarised',ref_prefix='F',num_units=1,fplist=['CP*', 'SM*'],do_erc=True,footprint='Capacitors_SMD:C_1206',pins=[
            Pin(num='1',name='~',func=Pin.PWRIN,do_erc=True),
            Pin(num='2',name='~',func=Pin.PWROUT,do_erc=True)]),
        Part(name='USB_OTG',dest=TEMPLATE,tool=SKIDL,keywords='connector USB USB_OTG USB_mini USB_micro',description='USB micro/mini connector',ref_prefix='J',num_units=1,fplist=['USB*'],do_erc=True,footprint='Capacitors_SMD:C_1206',pins=[
            Pin(num='1',name='VBUS',func=Pin.PWROUT,do_erc=True),
            Pin(num='2',name='D-',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='D+',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='ID',func=Pin.PWRIN,do_erc=True),
            Pin(num='5',name='GND',func=Pin.PWRIN,do_erc=True),
            Pin(num='6',name='shield',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='CRYSTAL_SMD',dest=TEMPLATE,tool=SKIDL,ref_prefix='X',num_units=1,do_erc=True,footprint='Crystals:Crystal_SMD_5032_4Pads',pins=[
            Pin(num='1',name='1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='2',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='case',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='SW_PUSH',dest=TEMPLATE,tool=SKIDL,keywords='Switch',description='Button',ref_prefix='SW',num_units=1,do_erc=True,footprint='Buttons_Switches_SMD:SW_SPST_EVQP0',pins=[
            Pin(num='1',name='1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='2',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='CONN_01X05',dest=TEMPLATE,tool=SKIDL,keywords='connector',description='Connector, single row, 01x05',ref_prefix='J',num_units=1,fplist=['Pin_Header_Straight_1X*', 'Pin_Header_Angled_1X*', 'Socket_Strip_Straight_1X*', 'Socket_Strip_Angled_1X*'],do_erc=True,footprint='Connectors_JST:JST_SH_SM05B-SRSS-TB_05x1.00mm_Angled',pins=[
            Pin(num='1',name='P1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='P2',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='P3',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='P4',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='P5',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='CONN_02X03',dest=TEMPLATE,tool=SKIDL,keywords='connector',description='Connector, double row, 02x03',ref_prefix='J',num_units=1,fplist=['Pin_Header_Straight_2X*', 'Pin_Header_Angled_2X*', 'Socket_Strip_Straight_2X*', 'Socket_Strip_Angled_2X*'],do_erc=True,footprint='Connectors_JST:JST_SH_SM06B-SRSS-TB_06x1.00mm_Angled',pins=[
            Pin(num='1',name='P1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='P2',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='P3',func=Pin.PASSIVE,do_erc=True),
            Pin(num='4',name='P4',func=Pin.PASSIVE,do_erc=True),
            Pin(num='5',name='P5',func=Pin.PASSIVE,do_erc=True),
            Pin(num='6',name='P6',func=Pin.PASSIVE,do_erc=True)]),
        Part(name='CONN_01X03',dest=TEMPLATE,tool=SKIDL,keywords='connector',description='Connector, single row, 01x03',ref_prefix='J',num_units=1,fplist=['Pin_Header_Straight_1X*', 'Pin_Header_Angled_1X*', 'Socket_Strip_Straight_1X*', 'Socket_Strip_Angled_1X*'],do_erc=True,footprint='Connectors_JST:JST_SH_SM03B-SRSS-TB_03x1.00mm_Angled',pins=[
            Pin(num='1',name='P1',func=Pin.PASSIVE,do_erc=True),
            Pin(num='2',name='P2',func=Pin.PASSIVE,do_erc=True),
            Pin(num='3',name='P3',func=Pin.PASSIVE,do_erc=True)])])