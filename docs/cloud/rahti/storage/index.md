# Available storage options

Pods are expendable. When they die, all state that was stored in the pod's own filesystems is lost. Pods are also meant to die and be replaced as part of normal operations such as a rolling update triggered by a deployment. In addition, by design no file written into a container, can leave the container.

