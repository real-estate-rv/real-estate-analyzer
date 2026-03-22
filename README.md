# Real Estate Investment Decision Tool

Outil complet d'analyse d'investissement immobilier Section 8 aux USA.

## Démarrage rapide

git clone https://github.com/real-estate-rv/real-estate-analyzer.git
cd real-estate-analyzer
cp .env.example .env
docker-compose up -d

## Architecture

### Backend
- FastAPI (Python)
- PostgreSQL + SQLAlchemy ORM
- Redis cache
- 35+ KPIs financiers

### Frontend
- React + TypeScript
- Tailwind CSS
- Dashboard propriétés

### Infrastructure
- Docker Compose (6 services)
- PostgreSQL 15 Alpine
- Redis 7 Alpine
- Nginx reverse proxy
- pgAdmin

## Villes cibles
- Cleveland, OH
- Birmingham, AL
- Montgomery, AL
- Mobile, AL
- Huntsville, AL

## Commandes utiles
docker-compose up -d
docker-compose down
docker-compose logs -f
docker-compose exec backend bash

## Licence
MIT
