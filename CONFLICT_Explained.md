### CONFLICT (add/add) Explained

- Cause: You independently created files with the same name both on the remote and locally.

- Solution:
  1. Manually resolve the conflict by using markers like `<<<<<<< HEAD` within the file as guides.
  2. Use `git add` to tell Git about the changes.
  3. Use `git commit` to finalize the merge.