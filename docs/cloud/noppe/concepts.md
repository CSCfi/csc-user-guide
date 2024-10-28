# Concepts

This document defines terminology in Noppe service.

Noppe is a CSC cloud service for interactive web based applications

## Application template

- Created by Admin
- Defines Application container image and configuration
- Defines resource limits (such as memory)
- See [the source code for images](https://github.com/CSCfi/noppe-public-images/tree/master/builds){target="_blank"} 
  for technical details

## Application

- Predefined content for one learning session
- Based on a Docker container - either JupyterLab or RStudio
- Created by Workspace manager based on Application template

## Application session aka Session

- One running copy of an Application
- Started and managed by User
- Has lifetime set by Application

## Workspace

- A container for Applications and Users
- Tied to a Cluster
- Has an Owner
- May have Co-owners
- Has a lifetime
- May contain persistent folders (Workspace `shared`, Users' `my-work`). See [Storage in Noppe](data_persistence.md)
- Has a maximum number of Applications (10 by default)
- Has a limit for total memory for concurrent sessions

## My Work folder

- Private directory per user per workspace, storing data between Application session launches
- Available in the Application session (if enabled by Owner) as `$HOME/my-work`
- Is tied to a Workspace
- Has lifetime tied to a Workspace

## Workspace shared folder

- Shared directory available to all users in a Workspace
- Is writable only by Workspace manager
- Is tied to a workspace
- Has lifetime tied to a Workspace
- Note that notebook files should not be executed within "shared" but rather moved to "my-work" folder

## Join code

- Unique Code generated for each workspace
- Workspace owner distributes this code for users to join the workspace

## End user

- A Workspace member or a user of public Applications
- Is authenticated
- May launch Application sessions
- Has access to public Applications
- May be part of Workspaces
- Has access to Workspace Applications through membership

## Workspace owner

- User that owns Workspaces or has been assigned Quota to create Workspaces 
- Principal of the Workspace
- Creates Workspace and the content in the Workspace for the workspace members
- May invite Users to become members in a workspace by sharing the Join code
- May promote members to Co-owners
- May demote Co-owners to members
- May add Applications based on Applications templates

## Workspace co-owner

- Can create content in the Workspace
- May promote members to Co-owners
- May demote Co-owners to members
- May invite users to become members in a workspace by sharing the join code
- May add Applications based on Applications templates

## Admin

- System administrator at CSC
- Has full rights in the system

## Cluster

- A resource for executing the Application sessions
- In practice: some sort of Kubernetes cluster in CSC cloud
- Configured by Admin
