from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from main_app.models import CustomUser, Admin, Staff, Student, Course, Subject, Session

User = get_user_model()

class Command(BaseCommand):
    help = 'Adds sample data for testing'

    def handle(self, *args, **kwargs):
        # Create Admin if not exists
        if not User.objects.filter(email='admin@example.com').exists():
            admin_user = User.objects.create_user(
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User',
                user_type='1'
            )
            Admin.objects.create(admin=admin_user)
            self.stdout.write(self.style.SUCCESS('Admin user created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))

        # Create Staff if not exists
        if not User.objects.filter(email='staff@example.com').exists():
            staff_user = User.objects.create_user(
                email='staff@example.com',
                password='staff123',
                first_name='Staff',
                last_name='User',
                user_type='2'
            )
            Staff.objects.create(admin=staff_user)
            self.stdout.write(self.style.SUCCESS('Staff user created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Staff user already exists'))

        # Create Student if not exists
        if not User.objects.filter(email='student@example.com').exists():
            student_user = User.objects.create_user(
                email='student@example.com',
                password='student123',
                first_name='Student',
                last_name='User',
                user_type='3'
            )
            Student.objects.create(admin=student_user)
            self.stdout.write(self.style.SUCCESS('Student user created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Student user already exists'))

        # Create Course if not exists
        if not Course.objects.filter(name='Computer Science').exists():
            course = Course.objects.create(
                name='Computer Science',
                created_at='2024-01-01',
                updated_at='2024-01-01'
            )
            self.stdout.write(self.style.SUCCESS('Course created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Course already exists'))

        # Create Subject if not exists
        if not Subject.objects.filter(name='Python Programming').exists():
            subject = Subject.objects.create(
                name='Python Programming',
                course=Course.objects.get(name='Computer Science'),
                staff=Staff.objects.first(),
                created_at='2024-01-01',
                updated_at='2024-01-01'
            )
            self.stdout.write(self.style.SUCCESS('Subject created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Subject already exists'))

        # Create Session if not exists
        if not Session.objects.filter(start_year='2024-01-01').exists():
            session = Session.objects.create(
                start_year='2024-01-01',
                end_year='2024-12-31'
            )
            self.stdout.write(self.style.SUCCESS('Session created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Session already exists'))

        self.stdout.write(self.style.SUCCESS('Sample data check completed')) 