# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensor_msg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10sensor_msg.proto\"S\n\x0b\x42oundingBox\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x02(\x05\x12\t\n\x01x\x18\x03 \x02(\x05\x12\t\n\x01y\x18\x04 \x02(\x05\x12\t\n\x01w\x18\x05 \x02(\x05\x12\t\n\x01h\x18\x06 \x02(\x05\"}\n\"JointPositionVelocitySensorMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\ttimestamp\x18\x02 \x02(\x01\x12\x14\n\x0cseg_run_time\x18\x03 \x02(\x01\x12\x0e\n\x06joints\x18\x04 \x03(\x01\x12\x12\n\njoint_vels\x18\x05 \x03(\x01\"\x97\x01\n!PosePositionVelocitySensorMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\ttimestamp\x18\x02 \x02(\x01\x12\x14\n\x0cseg_run_time\x18\x03 \x02(\x01\x12\x10\n\x08position\x18\x04 \x03(\x01\x12\x12\n\nquaternion\x18\x05 \x03(\x01\x12\x17\n\x0fpose_velocities\x18\x06 \x03(\x01\"U\n\x1aJointVelocitySensorMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\ttimestamp\x18\x02 \x02(\x01\x12\x18\n\x10joint_velocities\x18\x03 \x03(\x01\"K\n\x1aJointPositionSensorMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\ttimestamp\x18\x02 \x02(\x01\x12\x0e\n\x06joints\x18\x03 \x03(\x01\"`\n\x19PosePositionSensorMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\ttimestamp\x18\x02 \x02(\x01\x12\x10\n\x08position\x18\x03 \x03(\x01\x12\x12\n\nquaternion\x18\x04 \x03(\x01\"]\n\x1e\x43\x61rtesianVelocitySensorMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\ttimestamp\x18\x02 \x02(\x01\x12\x1c\n\x14\x63\x61rtesian_velocities\x18\x03 \x03(\x01\"K\n\x1cShouldTerminateSensorMessage\x12\x11\n\ttimestamp\x18\x01 \x02(\x01\x12\x18\n\x10should_terminate\x18\x02 \x02(\x08\"\x83\x01\n\x1f\x43\x61rtesianImpedanceSensorMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\ttimestamp\x18\x02 \x02(\x01\x12!\n\x19translational_stiffnesses\x18\x03 \x03(\x01\x12\x1e\n\x16rotational_stiffnesses\x18\x04 \x03(\x01\"n\n\x1a\x46orcePositionSensorMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\ttimestamp\x18\x02 \x02(\x01\x12\x14\n\x0cseg_run_time\x18\x03 \x02(\x01\x12\x0c\n\x04pose\x18\x04 \x03(\x01\x12\r\n\x05\x66orce\x18\x05 \x03(\x01\"\xc0\x01\n$ForcePositionControllerSensorMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\ttimestamp\x18\x02 \x02(\x01\x12\x19\n\x11position_kps_cart\x18\x03 \x03(\x01\x12\x16\n\x0e\x66orce_kps_cart\x18\x04 \x03(\x01\x12\x1a\n\x12position_kps_joint\x18\x05 \x03(\x01\x12\x17\n\x0f\x66orce_kps_joint\x18\x06 \x03(\x01\x12\x11\n\tselection\x18\x07 \x03(\x01\"m\n\"JointTorqueControllerSensorMessage\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\ttimestamp\x18\x02 \x02(\x01\x12\x11\n\tselection\x18\x03 \x03(\x01\x12\x15\n\rjoint_torques\x18\x04 \x03(\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sensor_msg_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOUNDINGBOX._serialized_start=20
  _BOUNDINGBOX._serialized_end=103
  _JOINTPOSITIONVELOCITYSENSORMESSAGE._serialized_start=105
  _JOINTPOSITIONVELOCITYSENSORMESSAGE._serialized_end=230
  _POSEPOSITIONVELOCITYSENSORMESSAGE._serialized_start=233
  _POSEPOSITIONVELOCITYSENSORMESSAGE._serialized_end=384
  _JOINTVELOCITYSENSORMESSAGE._serialized_start=386
  _JOINTVELOCITYSENSORMESSAGE._serialized_end=471
  _JOINTPOSITIONSENSORMESSAGE._serialized_start=473
  _JOINTPOSITIONSENSORMESSAGE._serialized_end=548
  _POSEPOSITIONSENSORMESSAGE._serialized_start=550
  _POSEPOSITIONSENSORMESSAGE._serialized_end=646
  _CARTESIANVELOCITYSENSORMESSAGE._serialized_start=648
  _CARTESIANVELOCITYSENSORMESSAGE._serialized_end=741
  _SHOULDTERMINATESENSORMESSAGE._serialized_start=743
  _SHOULDTERMINATESENSORMESSAGE._serialized_end=818
  _CARTESIANIMPEDANCESENSORMESSAGE._serialized_start=821
  _CARTESIANIMPEDANCESENSORMESSAGE._serialized_end=952
  _FORCEPOSITIONSENSORMESSAGE._serialized_start=954
  _FORCEPOSITIONSENSORMESSAGE._serialized_end=1064
  _FORCEPOSITIONCONTROLLERSENSORMESSAGE._serialized_start=1067
  _FORCEPOSITIONCONTROLLERSENSORMESSAGE._serialized_end=1259
  _JOINTTORQUECONTROLLERSENSORMESSAGE._serialized_start=1261
  _JOINTTORQUECONTROLLERSENSORMESSAGE._serialized_end=1370
# @@protoc_insertion_point(module_scope)
