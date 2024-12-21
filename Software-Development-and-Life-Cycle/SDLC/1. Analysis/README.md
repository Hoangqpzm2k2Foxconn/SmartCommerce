
# SmartCommerce API Documentation

## Overview
This document provides detailed information about the SmartCommerce API endpoints.

## Authentication
API uses JWT for authentication. Include the JWT token in the Authorization header:
```
Authorization: Bearer <token>
```

## Endpoints

### Payment API
- POST /api/payment/create/
- GET /api/payment/verify/{payment_id}/

### Courses API
- GET /api/courses/
- POST /api/courses/enroll/

### Marketplace API
- GET /api/marketplace/products/
- POST /api/marketplace/purchase/
