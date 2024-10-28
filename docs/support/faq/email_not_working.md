# Sending email when a job starts/finishes is not working

* Check that the option is correctly set in your batch script. For example, to
  get email when the job starts, it should read `#SBATCH --mail-type=BEGIN`.
* Multiple arguments are separated by a comma, e.g.
  `#SBATCH --mail-type=BEGIN,END`.
* The email is by default sent to the email address linked to your CSC account.
* If you are using the `#SBATCH --mail-user=<your email address>` option to
  override the default email address, ensure that the email set is valid.
