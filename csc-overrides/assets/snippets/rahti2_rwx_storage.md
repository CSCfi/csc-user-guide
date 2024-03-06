!!! error-label

    The only storage class currently available for now is *standard-csi*, which is ReadWriteOnce (RWO). This means that only one Pod can have a Persitent Volume Claim at a time. We are working on providing a new storage class that supports ReadWriteMany (RWX, multi attach).