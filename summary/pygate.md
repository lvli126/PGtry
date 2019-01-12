
# 1. pygate生成mac文件

## 1.1 Geometry
```
Geometry(World: Physics_Box
           camera: Camera
            phantom: Phantom
            surface: Surface	
           )

Logistic_Box(shape: Vector,   
             origin: Vector,  
             normal: Vector)#from dxl.shape  

Vector(x,y,z: float)#from dxl.shape

Vec3(x, y, z: float or int ,
     unit: string)
```
```
Volume(name: string
       material: string
       mother: string
       position: Vec3 
       unit: string or none(默认"mm")
       repeaters: Repeater)
```
Volume子类:
```
Physics_Box(name: string
            size: Vec3 or none
            material: string
            mother: string
            position: Vec3 or none
            unit: none or string(默认"mm")
            repeaters: Repeater
            box_from_shape: None or Logistic_Box(若size，position是none，则该量必须是Logistic_box))  
Cylinder(name: string
        rmax: float
        rmin: float
        height:
        phi_start:
        delta_phi:
        material: string(from MaterialDatabase.db), 
        mother: string, 
        position: Vec3, 
        unit: string or none(默认"mm"), 
        repeaters: Repeater)
Sphere(name: string
       rmax: float
       rmin: float
       phi_start:
       delta_phi:
       theta_start:
       delta_theta:
       material: string, 
       mother: string, 
       position: Vec3, 
       unit: string or none(默认"mm"), 
       repeaters: Repeater or None)
ImageRegularParamerisedVolume(name: string,
                              image_file: url, 
                              range_file: url,
                              material: string, 
                              mother: string, 
                              position: Vec3, 
                              unit: string or none(默认"mm"), 
                              repeaters: Repeater or None)
Patch(name: string, 
      patch_file, 
      material: string, 
      mother: string, 
      position: Vec3, 
      unit: string or none(默认"mm"), 
      repeater: None or Repeater)
```

Repeater与子类：
```
Repeater
RingRepeater
CartesianRepeater()#from dxl.shape

RepeaterRing(number: integer
             ring_repeater: RingRepeater)
RepeaterLinear(number: integer,
               steps: Vec3, 
               linear_repeater: CartesianRepeater, 
               unit: string or none(默认"mm"))
RepeaterCubic(grids: Vec3, 
              steps: Vec3, 
              cartesian_repeater: CartesianRepeater, 
              unit: string or none(默认"mm"))
```
```
Camera(system: System
       sensitive_detectors: Tuple[Volume]=())
```
system与其子类：
```
System(name:string
       attach_systems: list: string)

PETscanner(level1: Physics_Box,                   
            level2, 
            level3, 
            level4, 
            level5, 
            sensitive_detectors: Tuple[Volume]=())
Ecat(block: Physics_Box, 
        crystal: Physics_Box)
CylindricalPET(rsector: Physics_Box, 
                module: Physics_Box, 
                submodule: Physics_Box or none, 
                crystal: Physics_Box,
                layer0: Physics_Box, 
                layer1: Physics_Box, 
                layer2: Physics_Box or None, 
                layer3: Physics_Box or None)
MultiPatchPET(container: Sphere       
                patch_list: Patch)
SPECThead(crystal, pixel: Physics_Box)
OpticalSystem(crystal, pixel: Physics_Box)
```
```
Phantom(sensitive_detectors：Tuple[Volume]=())
```
surface与其2子类: 
```
Surface (name: string,
         base: Volume, 
         insert: Volume)

SurfacePerfectAPD(name: string,
                    base: Volume, 
                    insert: Volume)
SurfaceRoughTeflonWrapped(name: string,
                            base: Volume, 
                            insert: Volume)
```
## 1.2 Digitizers
```
Digitizers()
```
insertable与子类：
```
Insertable(name: string, 
           is_define_name: bool= False(这里是类中直接给定false，子类也不变), 
           is_explicit_insert: bool = True)

Singles
    子类：
    SinglesChain(name: string, 
                 is_define_name: bool=True)
```
```
Adder与子类（在日常仿真中不变）
Adder 不变
AdderCompton 不变
AdderOptical 不变
```
```
Readout(policy: None | string: TakeEnergyWinne(若为none的默认方法), TakeEnergyCentroid,                  
        depth: integer(在默认policy下，一般ECAT=1, CylindricalPET=2，其他要视情况定)
        name='readout', 
        is_define_name=False)
Blurring(law: string: inverseSquare, linear, ... ,
         resolution: float(默认0.15), 
         eor=511, 
         slope=None,
         name='blurring', 
         is_define_name=False)
```
holder与2子类；
```
Holder(value: float, 
       name: string, 
       is_define_name=False)
ThresHolder(value: float, 
            name='thresholder')
UpHolder(value: float(>ThresHolder.value), 
         name='upholder')
```
```
TimeResolution(resolution: float, 
               name: string, 
               is_define_name=False)
```
WithBuffer与子类：
```
WithBuffer
MemoryBuffer
DeadTime(volume: string(Ecat=block; CylindricalPET=module), 
        t: float(ps), 
        mode: string, 
        buffer_size, 
        buffer_mode, 
        name='deadtime', 
        is_define_name=False)
DeadTimeMulti(同deadtime, name变成‘deadtimeMulti’)
```
```
CoincidenceSorter(input_=none,                                  
                  window: float, 
                  offset: float(默认0 ns，不变), 
                  name='Coincidences', 
                  is_define_name=False, 
                  is_explicit_insert = False)
CoincidencesChain(input1: none,                                 
                  input2: none, 
                  name, 
                  plugins = None, 
                  use_priority=None, 
                  conserve_all_event = None, 
                  is_define_name=True)
```

## 1.3 Physics	不变


## 1.4 Source
```
Source(name: string,
       particle: Particle, 
       activity: str | int | float | list | tuple:
                (str: directly attached
                int, float: add default unit becquerel
                list, tuple: [0]: value, [1]: unit)
       angle: AngularISO,
       shape: Shape, 
       position: Vec3)
```
Particle与子类：
```
Particle(unstable: bool,   不变
         halflife: float)    
ParticlePositron(unstable=True, halflife=6586) 不变
ParticleGamma(unstable=True, 
              halflife=6586.2,  不变
              monoenergy=511, 
              back2back=True)
```
Angular与子类：
```
Angular  
AngularISO(ang: array: float=[0, 180, 0, 360])(前两个表示发射角度与向上方向轴的角度，范围是0-180；后两个是与transaxial平面的角度，范围0-360)
```
```
Shape(dimension: string)
    子类：
    ShapePlane(dimension='Plane') 不变
        子类：
        Circle(radius: float| int)
        Annulus(radius0, radius: float| int)
        Ellipse(half_size: List: float| int)
        Rectangle(half_size: List: float| int)
    Voxelized(read_table: string: url, 
              read_file: string: url,
              reader='interfile', 不变
              translator='range', 不变
              position: Vec3)
    Ellipsoid(half_size: Vec3, 
              dimension)
    Sphere(radius: int|float, 
           dimension)
    ShapeSurfaceOrVolume(dimension = 'Surface' or 'Volume')
        子类：
        Cylinder(radius: int|float, 
                 halfz: list: int|float, 
                 dimension: string:'Surface' or 'Volume')
```
```
SourceList(sources: List: Source)
```

## 1.5 Parameter
```
Parameter(random_engine: RandomEngine, 
          outputs: List: Output, 
          acquisition: Acquisition)
```
RandomEngine与子类：
```
RandomEngine(seed: str='default'(一般设置成auto)) 不变
    
    RandomEngineRanlux64        engine_type = 'Ranlux64'
    RandomEngineJamesRandom     engine_type = 'JamesRandom'
    RandomEngineMersenneTwister engine_type = 'MersenneTwister'
```
Output与子类：
```
Output(file_name: str)
Ascii(file_name: str, 
        hit: bool=0 or 1 , 
        singles: bool=0 or 1, 
        coincidences: bool=0 or 1)
Binary(同ascii)
Root(file_name: str,
        hit: bool= 0 or 1, 
        singles: bool= 0 or 1, 
        coincidences: bool= 0 or 1, 
        optical: bool= 0 or 1, 
        delay: bool= 0 or 1)
Sinogram    一般不用这种形式，会爆内存
```
Acquisition与子类：
```
Acquisition
AcquisitionPrimaries(number: int=10000)
AcquisitionPeriod(start: float=0.0, 
                  end: float=1.0, 
                  step: float=1.0)（step要能被end-start整除）
```

## 1.6 Material
```
MaterialDatabase(path: str)
MaterialDatabaseLocal(path: str)
```

## 1.7 visualition
```
Visualisation(is_disable: bool=True or False)#默认true
```

# 2. pygate仿真
```
pygate generate -t/--target script_name -c/--config config_name -o/--output mac_name

pygate init subdir -n number: int

pygate init bcast

pygate submit

pygate clean –d remove subdirectories
             -f remove files in work directory
             -s remove *.out *.err files

pygate merge --target result.root --method had

squeue
```
