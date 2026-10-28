# AGENTS.md — PANDUAN KERJA ASISTEN AI SKINCHECK

## 🚨 MANDATORY DATABASE RULE: XAMPP MYSQL ONLY
This project **MUST ALWAYS USE XAMPP MYSQL** (`skincheck_db`), **NEVER SQLITE**.

### Rules for Agents:
1. File `.env` MUST HAVE:
   ```env
   DB_CONNECTION=mysql
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DB_DATABASE=skincheck_db
   DB_USERNAME=root
   DB_PASSWORD=
   ```
2. Do not change `DB_CONNECTION` back to `sqlite`.
3. All migrations, models, seeds, and unit tests run against MySQL in XAMPP.
4. If testing or restarting tables, run:
   ```powershell
   python setup_db.py
   ```
5. Data migration helper:
   ```powershell
   python migrate_sqlite_to_mysql.py
   ```
