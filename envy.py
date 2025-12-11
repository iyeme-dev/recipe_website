import os

# Use your real Neon URL here (replace YOUR_PASSWORD with the real password)
os.environ["DATABASE_URL"] = "postgresql://neondb_owner:YOUR_PASSWORD@ep-flat-scene-agrmwosh.c-2.eu-central-1.aws.neon.tech/bloat_curse_swipe_942866"

# Simple assignment is fine here
os.environ["SECRET_KEY"] = "django-insecure-g0_y5rixo!!%_0y^d((axwsx4@-)xf=tf=mcsnp70ff!#cmveg"

# Turn Django debug ON locally so you can see full error pages
os.environ["DEBUG"] = "True"
