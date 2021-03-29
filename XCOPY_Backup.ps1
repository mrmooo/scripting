net use F: \\backup\backup MOOMOOMOOMOOMOOMOO /user:backup\MOO /persistent:yes; get-date >> E:\BACKUP\backup_log_$(get-date -f yyyy-MM-dd).txt; xcopy \\backup\backup E:\BACKUP /E /D /Y /F /V >> E:\BACKUP\backup_log_$(get-date -f yyyy-MM-dd).txt
# Replace MOO with the appropriate password and username.
