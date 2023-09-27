## Library Management

building own app

#### License

MIT

commands to install and create the app (assuming that are the pre requisite are already installed)

bench init frappe-bench --frappe-path https://github.com/frappe/frappe --frappe-branch version-13 --python=python3.8 --verbose

cd frappe-bench

bench new-app library_management

./env/bin/pip install -q -U -e ./apps/library_management

bench build

bench new-site library.test

bench --site library.test add-to-hosts

bench --site library.test install-app library_management

bench --site library.test list-apps

~set a dummy password for inital login~

bench --site library.test set-admin-password pass@123

bench --site library.test console

bench --site library.test mariadb

bench set-config -g developer_mode true

url to access app sites:
http://library.test:8000/app
