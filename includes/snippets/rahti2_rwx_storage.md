!!! error-label

    The only storage class currently available for now is *standard-csi*, which is ReadWriteOnce (RWO). This means that a Persistent Volume Claim can only be attached to a single Pod at a time. We are working on providing a new storage class that supports ReadWriteMany (RWX, multi attach).