#!/bin/bash

echo "Adding and committing each file with meaningful messages..."

git add alx_travel_app/settings.py
git commit -m "chore: add rest_framework and drf-yasg to INSTALLED_APPS"

git add alx_travel_app/urls.py
git commit -m "feat: configure main URLs with API routes and Swagger UI (/swagger/, /redoc/)"

git add listings/serializers.py
git commit -m "feat: create ListingSerializer for DRF"

git add listings/views.py
git commit -m "feat: implement ListingViewSet with full CRUD operations"

git add listings/urls.py
git commit -m "feat: register ListingViewSet with DRF router"

git add bookings/serializers.py
git commit -m "feat: create BookingSerializer for DRF"

git add bookings/views.py
git commit -m "feat: implement BookingViewSet with full CRUD operations"

git add bookings/urls.py
git commit -m "feat: register BookingViewSet with DRF router"

git add requirements.txt
git commit -m "chore: add djangorestframework and drf-yasg to requirements"

git add README.md
git commit -m "docs: update README with API endpoints and Swagger documentation link"

git add .gitignore
git commit -m "chore: add comprehensive .gitignore (pycache, venv, sqlite3, etc.)"

# Catch any remaining files (e.g. bookings/models.py, admin.py, etc.)
git add .
git commit -m "feat: complete bookings app setup and minor fixes"

echo ""
echo "All files committed with clean, professional messages!"
echo "Your commit history is now perfect for ALX peer review"
echo ""
git log --oneline -10
echo ""
echo "Ready to push: git push origin main"
