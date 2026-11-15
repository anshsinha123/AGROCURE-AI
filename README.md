# AGROCURE AI – COMPLETE ADMIN PANEL DEVELOPMENT PROMPT

Act as a senior full-stack developer, UI/UX designer, database architect, and security engineer.

I already have a project called AGROCURE AI, an AI-powered plant disease detection website that detects diseases in Tomato, Potato, Capsicum, and Grapes using leaf images.

I want you to develop a complete, professional, fully functional ADMIN PANEL for this existing application.

IMPORTANT: Do not create a separate disconnected demo. Integrate the Admin Panel with my existing frontend, backend, MongoDB database, authentication system, and ML prediction service.

## 1. ADMIN PANEL DESIGN

Create a premium, modern agricultural technology dashboard.

Design requirements:
- Forest Green: #14532D
- Leaf Green: #22C55E
- White background
- Light green cards
- Professional typography (Poppins or Inter)
- Modern sidebar navigation
- Responsive dashboard
- Interactive charts
- Professional tables
- Search and filtering
- Smooth transitions
- Dark mode option

Admin layout:
- Left sidebar
- Top navigation bar
- Main dashboard
- Notification section
- Admin profile menu
- Logout button

## 2. ADMIN LOGIN AND SECURITY

Create a separate secure admin login system.

Features:
- Admin email and password
- JWT authentication
- Password hashing using bcrypt
- Role-based access control
- Admin-only protected routes
- Session expiration
- Logout
- Unauthorized access prevention

Roles:
1. Super Admin
2. Admin
3. Content Manager

Only authorized administrators can access admin functions.

Never allow users to become administrators by changing frontend values or submitting their own role.

## 3. ADMIN DASHBOARD

Create a real-time dashboard displaying:

Statistics cards:
- Total registered users
- Total plant scans
- Total healthy predictions
- Total disease predictions
- Total Tomato scans
- Total Potato scans
- Total Capsicum scans
- Total Grapes scans
- Total active users
- Total feedback received

Charts:
- Daily prediction statistics
- Monthly scan statistics
- Crop-wise prediction distribution
- Disease-wise distribution
- Healthy vs diseased comparison
- User registration growth

All dashboard statistics must come from MongoDB APIs. Do not use hardcoded demo statistics.

## 4. USER MANAGEMENT

Create a complete user management module.

Admin should be able to:

- View all registered users
- Search users by name and email
- Filter users by registration date
- View individual user profiles
- View user scan history
- View user activity
- Activate or deactivate accounts
- Delete accounts with confirmation
- Export user data to CSV

Display:
- User ID
- Name
- Email
- Registration date
- Total scans
- Account status

Never display users' passwords or password hashes.

## 5. AI PREDICTION MANAGEMENT

Create a dedicated AI prediction monitoring page.

Admin should be able to:

- View all plant disease predictions
- View uploaded leaf images
- View predicted crop
- View predicted disease
- View confidence percentage
- View prediction timestamp
- Search by disease name
- Filter by crop
- Filter by prediction date
- Filter healthy and infected results
- View individual prediction details

Provide analytics for:
- Most frequently detected diseases
- Most scanned crops
- Low-confidence predictions
- Prediction volume over time

Admin must not be able to modify historical AI prediction results without an auditable correction process.

## 6. DISEASE MANAGEMENT

Create a complete disease database management module.

Admin can:
- Add new disease information
- Edit disease information
- Delete disease records
- View all diseases
- Search diseases
- Filter diseases by crop

Disease information fields:
- Disease name
- Crop name
- Scientific name
- Disease description
- Symptoms
- Causes
- Disease severity information
- Prevention methods
- Reference images
- Status

Support Tomato, Potato, Capsicum and Grapes.

Keep disease information separate from the ML model's class mapping. Adding a disease article must not automatically change the model's supported classes.

## 7. ORGANIC TREATMENT MANAGEMENT

Create an Organic Solutions management module.

Admin can:
- Add organic treatments
- Edit organic treatments
- Delete treatments
- Assign treatments to diseases
- Add treatment images
- Add application instructions
- Add precautions
- Add frequency information

Examples:
- Neem-based products
- Biofungicides
- Biological pest management
- Organic crop protection
- Natural prevention methods

## 8. INORGANIC TREATMENT MANAGEMENT

Create an Inorganic Solutions management module.

Admin can:
- Add chemical treatment information
- Edit treatment information
- Delete treatment records
- Assign chemical solutions to diseases
- Add active ingredients
- Add registered product details
- Add application instructions
- Add safety precautions
- Add protective equipment instructions
- Add pre-harvest interval information

IMPORTANT:
Never invent chemical dosage or recommend unregistered pesticides. Store verified product-label information and require administrator review before publishing treatment recommendations.

## 9. MULTILINGUAL CONTENT MANAGEMENT

Create a language management section.

Supported languages:
- English
- Hindi
- Bengali
- Punjabi
- Marathi
- Tamil
- Telugu

Admin should be able to:
- Manage translated disease descriptions
- Manage translated treatment information
- Edit translated content
- Publish translations
- Preview language changes

## 10. ML MODEL MANAGEMENT

Create a dedicated ML Model Monitoring section.

Display:
- Model name
- Model version
- Training date
- Number of supported classes
- Model file status
- Current active model
- Last deployment date
- Model accuracy, when verified test metrics are available

Features:
- Upload new model version
- Upload class_names.json
- Validate model and class mapping
- Activate a model version
- Roll back to previous version
- View model metadata
- View model evaluation metrics
- Monitor inference errors

Only allow validated models to become active.

Do not claim model accuracy based on training accuracy alone. Show test-set evaluation metrics separately.

## 11. FEEDBACK AND SUPPORT MANAGEMENT

Admin can:
- View all user feedback
- View user ratings
- Read feedback messages
- Search feedback
- Filter feedback by date
- Mark feedback as resolved
- Delete inappropriate feedback
- View contact messages
- Reply through an integrated notification or support system

## 12. NOTIFICATION MANAGEMENT

Create an admin notification system.

Admin can:
- Send announcements
- Send maintenance notifications
- Notify users about new features
- Send important disease-related awareness messages
- View notification history
- Schedule announcements

## 13. REPORTS AND ANALYTICS

Create a reports section.

Allow admin to:
- Generate daily reports
- Generate weekly reports
- Generate monthly reports
- Download PDF reports
- Export CSV reports
- View crop-wise analytics
- View disease-wise analytics
- View user growth reports
- View prediction confidence distribution

Reports must use actual database records.

## 14. SYSTEM SETTINGS

Create a settings module.

Features:
- Website name and logo management
- Admin profile settings
- Password change
- Language settings
- Notification settings
- Image upload limits
- Prediction confidence threshold
- Website maintenance mode
- API health monitoring
- Database connection status
- Backend service status
- ML service status

Changing the confidence threshold must affect the real prediction service only after validation and explicit saving.

## 15. ADMIN ACTIVITY LOGS

Create an audit logging system.

Record:
- Admin login
- Admin logout
- User activation/deactivation
- User deletion
- Disease additions and modifications
- Treatment changes
- Model uploads
- Model activation
- Settings changes

Each activity must store:
- Admin ID
- Action
- Description
- Timestamp
- Relevant record ID

Audit logs should be protected against ordinary administrator modification.

## 16. MONGODB DATABASE

Create the following collections or equivalent Mongoose models:

1. Admins
2. Users
3. Predictions
4. Diseases
5. OrganicTreatments
6. InorganicTreatments
7. Feedback
8. Notifications
9. ModelVersions
10. AdminActivityLogs
11. SystemSettings

Use proper validation, indexes, timestamps and relationships.

## 17. ADMIN BACKEND API ROUTES

Authentication:
- POST /api/admin/auth/login
- POST /api/admin/auth/logout
- GET /api/admin/auth/profile

Dashboard:
- GET /api/admin/dashboard/stats
- GET /api/admin/dashboard/analytics

Users:
- GET /api/admin/users
- GET /api/admin/users/:id
- PATCH /api/admin/users/:id/status
- DELETE /api/admin/users/:id

Predictions:
- GET /api/admin/predictions
- GET /api/admin/predictions/:id
- GET /api/admin/predictions/analytics

Diseases:
- GET /api/admin/diseases
- POST /api/admin/diseases
- PUT /api/admin/diseases/:id
- DELETE /api/admin/diseases/:id

Treatments:
- GET /api/admin/treatments
- POST /api/admin/treatments
- PUT /api/admin/treatments/:id
- DELETE /api/admin/treatments/:id

ML Models:
- GET /api/admin/models
- POST /api/admin/models/upload
- POST /api/admin/models/:id/activate
- POST /api/admin/models/:id/rollback

Feedback:
- GET /api/admin/feedback
- PATCH /api/admin/feedback/:id/status

Reports:
- GET /api/admin/reports/pdf
- GET /api/admin/reports/csv

Settings:
- GET /api/admin/settings
- PUT /api/admin/settings

Activity:
- GET /api/admin/activity-logs

Protect every admin API with authentication and role-based authorization.

## 18. ADMIN PANEL FOLDER STRUCTURE

Create a clean architecture:

admin/
  frontend/
    src/
      components/
        Sidebar.jsx
        Navbar.jsx
        StatCard.jsx
        DataTable.jsx
        Charts.jsx
      pages/
        AdminLogin.jsx
        Dashboard.jsx
        Users.jsx
        Predictions.jsx
        Diseases.jsx
        OrganicTreatments.jsx
        InorganicTreatments.jsx
        ModelManagement.jsx
        Feedback.jsx
        Notifications.jsx
        Reports.jsx
        Settings.jsx
        ActivityLogs.jsx
      services/
        adminApi.js
      context/
        AdminAuthContext.jsx

  backend/
    controllers/
    routes/
    middleware/
    models/
    services/
    utils/

Integrate these modules into my existing AGROCURE AI architecture rather than duplicating existing functionality.

## 19. FINAL REQUIREMENTS

The Admin Panel must:

- Work with real MongoDB data.
- Have fully functional buttons and forms.
- Have working search, sorting and filtering.
- Have secure admin authentication.
- Have role-based permissions.
- Have working CRUD operations.
- Have responsive layouts.
- Have loading and error states.
- Have confirmation dialogs for destructive actions.
- Have proper form validation.
- Have pagination for large datasets.
- Have audit logs.
- Have no fake statistics or dummy predictions.
- Have no dead buttons or placeholder functionality.

First inspect my existing project structure and reuse existing models, routes and services wherever possible.

Implement the Admin Panel step by step. Provide complete source code and explain how to run and test it locally.

Do not break the existing user-facing AGROCURE AI website.
