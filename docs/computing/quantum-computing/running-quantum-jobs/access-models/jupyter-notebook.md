# Jupyter notebook

The [LUMI web interface](https://docs.lumi-supercomputer.eu/runjobs/webui/){ target=_blank } can be used to run quantum jobs interactively in a Jupyter notebook. For logging in, see the [LUMI documentation](https://docs.lumi-supercomputer.eu/firststeps/loggingin-webui/){ target=_blank }.

1. From the dashboard, open the **Jupyter** app and select your project and partition. If you have an active reservation, select it under *Reservation*.
2. Under **Settings** click on **Advanced**, set **Custom Python type** to *Script*, and paste one of the scripts below into the **Script or paht to script** textbox. Replace `<DEVICE_VALUE>` with the identifier of your device, see [Runtime identifiers](../../devices/overview.md) on the device page.
3. Click **Launch**.

=== "Qiskit"

    ```bash
    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-qiskit
    export DEVICES=("<DEVICE_VALUE>")
    source $RUN_SETUP
    ```

=== "Cirq"

    ```bash
    module use /appl/local/quantum/modulefiles
    module load fiqci-vtt-cirq
    export DEVICES=("<DEVICE_VALUE>")
    source $RUN_SETUP
    ```

!!! info "Exporting multiple backend"
    You can export multiple backend using `export DEVICES=("<DEVICE_VALUE1>" "<DEVICE_VALUE2>")`. Make sure the devices have compatible software versions.

!!! info "Courses"
    If you are using the quantum computers during a course, a custom environment may have been prepared for it. In that case use the **Jupyter for courses** app instead.

    !["Quantum jobs with Jupyter for courses"](../../../img/helmi_with_jupyter_for_courses_gui.png)

See [Circuit job](../circuit-job.md) for an example circuit level job python script and [Pulse job](../pulse-job.md) for a Pulse level job example.

## Further Reading
* [Circuit level access](../circuit-job.md)
* [Pulse level access](../pulse-job.md)
* [Batch jobs](./batch.md)
* [Interactive jobs](srun.md)
* [LUMI Documentation](https://docs.lumi-supercomputer.eu/){ target=_blank }
