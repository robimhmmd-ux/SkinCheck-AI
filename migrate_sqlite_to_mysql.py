"""
Script untuk memigrasi data dari SQLite (skincheck_db.sqlite) ke MySQL (XAMPP).
Jalankan script ini setelah MySQL di XAMPP aktif dan konfigurasi .env disetel ke MySQL.
"""
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.config.database import Base
from app.models.user import User
from app.models.product import Product
from app.models.skin_scan import SkinScan
from app.models.analysis_result import AnalysisResult
from app.models.activity_log import ActivityLog
from app.models.otp_token import OTPToken
from app.models.system_setting import SystemSetting
import setup_db

def migrate():
    print("=== MIGRASI DARI SQLITE KE MYSQL (XAMPP) ===")
    
    # 1. Pastikan database MySQL siap
    setup_db.ensure_database_exists()
    
    # 2. SQLite source
    sqlite_url = "sqlite:///./skincheck_db.sqlite"
    sqlite_engine = create_engine(sqlite_url)
    SqliteSession = sessionmaker(bind=sqlite_engine)
    sqlite_db = SqliteSession()

    # 3. MySQL target
    password_part = f":{settings.DB_PASSWORD}" if settings.DB_PASSWORD else ""
    mysql_url = f"mysql+pymysql://{settings.DB_USERNAME}{password_part}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}"
    mysql_engine = create_engine(mysql_url)
    
    print("Membuat struktur tabel di MySQL...")
    Base.metadata.create_all(bind=mysql_engine)
    MysqlSession = sessionmaker(bind=mysql_engine)
    mysql_db = MysqlSession()

    try:
        # Migrasi Users
        users = sqlite_db.query(User).all()
        for u in users:
            existing = mysql_db.query(User).filter(User.id == u.id).first()
            if not existing:
                mysql_db.merge(u)
        mysql_db.commit()
        print(f"✓ Berhasil memindahkan {len(users)} data Users.")

        # Migrasi Products
        products = sqlite_db.query(Product).all()
        for p in products:
            existing = mysql_db.query(Product).filter(Product.id == p.id).first()
            if not existing:
                mysql_db.merge(p)
        mysql_db.commit()
        print(f"✓ Berhasil memindahkan {len(products)} data Products.")

        # Migrasi SkinScans
        scans = sqlite_db.query(SkinScan).all()
        for s in scans:
            existing = mysql_db.query(SkinScan).filter(SkinScan.id == s.id).first()
            if not existing:
                mysql_db.merge(s)
        mysql_db.commit()
        print(f"✓ Berhasil memindahkan {len(scans)} data SkinScans.")

        # Migrasi AnalysisResults
        results = sqlite_db.query(AnalysisResult).all()
        for r in results:
            existing = mysql_db.query(AnalysisResult).filter(AnalysisResult.id == r.id).first()
            if not existing:
                mysql_db.merge(r)
        mysql_db.commit()
        print(f"✓ Berhasil memindahkan {len(results)} data AnalysisResults.")

        # Migrasi ActivityLogs
        logs = sqlite_db.query(ActivityLog).all()
        for l in logs:
            existing = mysql_db.query(ActivityLog).filter(ActivityLog.id == l.id).first()
            if not existing:
                mysql_db.merge(l)
        mysql_db.commit()
        print(f"✓ Berhasil memindahkan {len(logs)} data ActivityLogs.")

        # Migrasi SystemSettings
        settings_list = sqlite_db.query(SystemSetting).all()
        for st in settings_list:
            existing = mysql_db.query(SystemSetting).filter(SystemSetting.key == st.key).first()
            if not existing:
                mysql_db.merge(st)
        mysql_db.commit()
        print(f"✓ Berhasil memindahkan {len(settings_list)} data SystemSettings.")

        print("\n✅ MIGRASI SELESAI DENGAN SUKSES!")
        print("Database SkinCheck sekarang berjalan penuh di XAMPP MySQL.")

    except Exception as e:
        print(f"\n❌ Terjadi kesalahan saat migrasi: {e}")
        mysql_db.rollback()
    finally:
        sqlite_db.close()
        mysql_db.close()

if __name__ == "__main__":
    migrate()
