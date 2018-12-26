import click

def kernel(config):
#    from pygate.predefined.simulations import  simulation, PredefinedSimulations
    from pygate.predefined.sources import sphere, Vec3
    from pygate.predefined._sources import plane_source
    from pygate.predefined._cameras import opticalsystem,optical_surfaces
    from pygate.predefined.parameters import optical_parameters
    from pygate.predefined.physics import optical_physics
    from pygate.predefined.digitizers import optical_digitizer
    from pygate.components.geometry.volume import Box,RepeaterCubic
    from pygate.components.geometry import Geometry
    from pygate.components.source import Rectangle,AngularISO
    from pygate.components.simulation import Simulation
    from pygate.components.parameter import Root,AcquisitionPeriod

    simu_name='OpticalSystem'
    world=Box('world',Vec3(100,100,100,'cm'))
#opticalsystem(world: Volume, box=None, crystal=None,rcp=None, pixel=None)
    box=Box(simu_name,Vec3(30.0,30.0,30.0,'cm'),position=Vec3(0.0,0.0,0.0,'mm'),material='Air',mother=world)
    crystal=Box('crystal',Vec3(3.0,3.0,2.0,'cm'),position=Vec3(0.0,0.0,1.0,'cm'),material='LYSO',mother=box)
#    cam=predefined._cameras.optical_gamma(world, crystal)
    cam=opticalsystem(world,
                      box=box,
                      crystal=crystal,
                      rcp=RepeaterCubic(Vec3(1, 1, 1), repeat_vector=Vec3(0.0, 0.0, 0.0, 'cm')),
                      pixel=Box('pixel',Vec3(3.0,3.0,2.0,'cm'),position=Vec3(0.0,0.0,-1.0,'cm'),material='G4_SILICON_DIOXIDE',mother=box))
    phan=()
    surf=optical_surfaces(cam)
    geo=Geometry(world,cam,phan,surf)
    src=plane_source(position=Vec3(0.0,0.0,4.0,'cm'),
                     src_name='plane_source',
                     rectangle=Rectangle([150, 150]),
                     activity=100,
                     particle=None,
                     angle=AngularISO([0,360,0,360]))
    mac = Simulation(geo,
                     physics=optical_physics(()),
                     digitizers=optical_digitizer(),
                     source=src,
                     parameter=optical_parameters(acqu=AcquisitionPeriod(0.0,5.0,1.0),
                                                  outputs=[Root('optical', 1, 1, None, 1, None), ])).render()

    return mac

@click.command()
@click.option('--config', '-c', help="mac maker config.", default=None)
@click.option('--output', '-o', help="output mac filename", default="main.mac")
def cli(config, output):
    content = kernel(config)
    with open(output, 'w') as fout:
        print(content, file=fout)

if __name__ == '__main__':
    cli()



