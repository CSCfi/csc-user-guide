# Sending email when a job starts/finishes is not working

- Check that the option is correctly set in your batchscript `#SBATCH --mail-type=BEGIN`
- Multiple arguments are separated by a comma `#SBATCH --mail-type=BEGIN,END`
- The email is sent to the email address of your csc account.
- If you are using the `--mail-user=` option, make sure the email set is valid.
