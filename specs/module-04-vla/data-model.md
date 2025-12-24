# Data Model: Module 4 – Vision–Language–Action (VLA)

## Overview
Data models for the Vision-Language-Action integration system that unifies speech, vision, and planning for humanoid robot autonomy.

**Created:** 2025-12-18
**Feature:** Module 4 – Vision–Language–Action (VLA)
**Status:** Complete

## Core Entities

### VoiceCommand
Represents a natural language command received by the system.

**Fields:**
- `id`: Unique identifier for the command
- `text`: The raw text of the command after speech recognition
- `timestamp`: When the command was received
- `confidence`: Confidence score of speech recognition (0.0-1.0)
- `intent`: Classified intent (navigation, manipulation, information, etc.)
- `entities`: Extracted entities (objects, locations, parameters)
- `context`: Environmental context at command time
- `status`: Processing status (received, processing, planned, executed, failed)

**Relationships:**
- One-to-many with `ActionSequence` (commands can generate multiple action sequences)

### ActionSequence
Represents a sequence of actions generated from a voice command.

**Fields:**
- `id`: Unique identifier for the sequence
- `command_id`: Reference to the originating VoiceCommand
- `actions`: Array of action specifications
- `status`: Execution status (planned, executing, completed, failed)
- `created_at`: Timestamp when sequence was generated
- `estimated_duration`: Estimated time to complete sequence
- `priority`: Priority level for execution scheduling

**Relationships:**
- Many-to-one with `VoiceCommand` (generated from a command)
- One-to-many with `ActionStep` (sequence contains multiple steps)

### ActionStep
Represents a single step in an action sequence.

**Fields:**
- `id`: Unique identifier for the step
- `sequence_id`: Reference to the parent ActionSequence
- `action_type`: Type of action (navigate, manipulate, perceive, respond)
- `parameters`: Action-specific parameters (target location, object ID, etc.)
- `dependencies`: Other steps this step depends on
- `status`: Execution status (pending, executing, completed, failed)
- `execution_result`: Result of execution (success, failure reason)
- `timestamp`: When step was executed

**Relationships:**
- Many-to-one with `ActionSequence` (part of a sequence)

### EnvironmentalState
Represents the current state of the environment.

**Fields:**
- `id`: Unique identifier for the state snapshot
- `timestamp`: When the state was captured
- `objects`: Array of recognized objects with positions
- `robot_pose`: Current robot position and orientation
- `navigation_map`: Available navigation locations
- `available_actions`: Actions the robot can currently perform
- `safety_constraints`: Current safety limitations

**Relationships:**
- One-to-many with `PerceptionData` (state contains perception data)

### PerceptionData
Represents data from various perception systems.

**Fields:**
- `id`: Unique identifier for the perception data
- `state_id`: Reference to the EnvironmentalState
- `sensor_type`: Type of sensor (camera, LIDAR, audio, etc.)
- `data_type`: Type of data (image, point cloud, audio, etc.)
- `timestamp`: When data was captured
- `location`: Where data was captured
- `confidence`: Confidence of perception results
- `content`: The actual perception data or results

**Relationships:**
- Many-to-one with `EnvironmentalState` (part of state)

## State Transitions

### VoiceCommand States
```
RECEIVED → PROCESSING → PLANNING → EXECUTING → COMPLETED
                    ↓
                 FAILED
```

- `RECEIVED`: Command captured from speech input
- `PROCESSING`: Natural language understanding in progress
- `PLANNING`: Action sequence being generated
- `EXECUTING`: Actions being executed
- `COMPLETED`: All actions completed successfully
- `FAILED`: Command could not be processed or executed

### ActionSequence States
```
PLANNED → EXECUTING → COMPLETED
    ↓         ↓
   FAILED ← FAILED_STEP
```

- `PLANNED`: Sequence generated, ready for execution
- `EXECUTING`: At least one step is executing
- `COMPLETED`: All steps completed successfully
- `FAILED`: Sequence could not be executed

### ActionStep States
```
PENDING → EXECUTING → COMPLETED
    ↓         ↓
   FAILED ← FAILED
```

- `PENDING`: Step waiting for dependencies
- `EXECUTING`: Step currently being executed
- `COMPLETED`: Step completed successfully
- `FAILED`: Step execution failed

## Validation Rules

### VoiceCommand Validation
- `text` must not be empty
- `confidence` must be between 0.0 and 1.0
- `timestamp` must be within reasonable time bounds
- `intent` must be from defined intent taxonomy

### ActionSequence Validation
- Must have at least one action in `actions` array
- All dependencies in `dependencies` must reference valid steps
- `estimated_duration` must be positive
- `priority` must be within defined range

### ActionStep Validation
- `action_type` must be from defined action type taxonomy
- `parameters` must match expected format for action type
- `sequence_id` must reference an existing sequence

### EnvironmentalState Validation
- `timestamp` must be recent (within defined window)
- `robot_pose` must be within navigable area
- `objects` must have valid spatial coordinates

## Relationships and Constraints

### VoiceCommand → ActionSequence
- One VoiceCommand can generate multiple ActionSequences
- ActionSequences must be completed or failed before command is considered processed
- ActionSequences inherit priority from parent VoiceCommand

### ActionSequence → ActionStep
- One ActionSequence contains multiple ActionSteps
- ActionSteps execute in dependency order
- ActionSequence status depends on all ActionStep statuses

### EnvironmentalState → PerceptionData
- One EnvironmentalState contains multiple PerceptionData entries
- PerceptionData provides the information for EnvironmentalState
- EnvironmentalState is updated when PerceptionData is processed

## Integration with ROS2 Messages

The data model maps to ROS2 message types where applicable:

- `VoiceCommand` ↔ Custom message for command interface
- `ActionStep` ↔ Various ROS2 action messages (navigation, manipulation)
- `EnvironmentalState` ↔ Robot state messages and sensor data
- `PerceptionData` ↔ Sensor messages (images, point clouds, etc.)

This mapping ensures compatibility with the ROS2 ecosystem while providing a structured data model for the VLA system.