=================
Blog Dashboard
=================

Horizon plugin for Mistral.

Setup Instructions
==================
This instruction assumes that Horizon is already installed and it's installation
folder is <horizon>. Detailed information on how to install Horizon can be
found at http://docs.openstack.org/developer/horizon/quickstart.html#setup.

The installation folder of Blog Dashboard will be referred to as <blog-dashboard>.

The following should get you started::

    $ sudo pip install -e <blog-dashboard>
    $ ln -s <blog-dashboard>/_50_blogs.py.example \
      <horizon>/openstack_dashboard/local/enabled/_50_blogs.py

Since Blog only supports Identity v3, you must ensure that the dashboard
points the proper OPENSTACK_KEYSTONE_URL in <horizon>/openstack_dashboard/local/local_settings.py file::

    OPENSTACK_API_VERSIONS = {
        "identity": 3,
    }

    OPENSTACK_KEYSTONE_URL = "http://%s:5000/v3" % OPENSTACK_HOST

When you're ready, you would need to either restart your apache::

    $ sudo service apache2 restart

or run the development server (in case you have decided to use local horizon)::

    $ cd ../horizon/
    $ tox -evenv -- python manage.py runserver


