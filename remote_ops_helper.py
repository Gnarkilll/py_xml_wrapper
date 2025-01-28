import os
import subprocess as sp

# TODO Implement logger instead of "print()"


class RemoteOperationException(Exception):
    pass


def execute(cmd):
    process = sp.Popen(cmd.split(), stdout=sp.PIPE)
    output, error = process.communicate()
    output = output.decode("utf-8")
    fail_words = ["fail", "failures", "failed"]
    if not process.returncode and any(word in output.lower() for word in fail_words):
        raise RemoteOperationException("\nERROR: {}\n".format(output))
    elif not process.returncode:
        print("Output: {}".format(output)) if output else print("Output: None")
    else:
        raise RemoteOperationException("Process was finished with exit code: {}\nERROR: {}\n".format(process.returncode, output))


def adb_push(local, remote):
    print("Push file")
    execute("adb push {} {}".format(local, remote))


def adb_install(pkg):
    print("Install package: {}".format(pkg))
    execute("adb shell pm install -g -t -r \"{}\"".format(pkg))


def run_test(test_group, test_name):
    print("Run test: {}_{}".format(test_group.lower(), test_name))
    app_runner = "com.here.apptester.test/android.support.test.runner.AndroidJUnitRunner"
    execute("adb shell am instrument -w -r -e debug false {}".format(app_runner))


def grant_permission(app, permission):
    # grant_permission("com.here.apptester", "WRITE_EXTERNAL_STORAGE")
    # grant_permission("com.here.apptester", "READ_EXTERNAL_STORAGE")
    print("Grant {} permission for app {}".format(permission, app))
    execute("adb shell pm grant {} android.permission.{}".format(app, permission))


def force_stop(app_name):
    print("Stop {}".format(app_name))
    execute("adb shell am force-stop {}".format(app_name))


def stop_apps():
    force_stop("com.here.apptester")
    force_stop("com.here.apptester.test")
    force_stop("com.here.functionaltestv2")


def copy_artifacts_on_desktop(test_name, test_class_name):
    root_dir = os.path.abspath(os.path.join(__file__, os.pardir))
    work_dir = "{}/output_artifacts/{}/{}".format(root_dir, test_class_name, test_name)

    print("Create artifacts directory for test: {}".format(test_name))
    execute("mkdir -p {}".format(work_dir))

    print("Copy artifacts")
    execute("adb pull /sdcard/Test/ {}".format(work_dir))

    cp_local("{}/Test/".format(work_dir), work_dir)
    rm_local("{}/Test".format(work_dir))


def rm_local(file_or_dir):
    print("Clear local: {}".format(file_or_dir))
    execute("rm -rf {}".format(file_or_dir))


def rm_remote(file_or_dir):
    print("Clear remote: {}".format(file_or_dir))
    execute("adb shell rm -rf {}".format(file_or_dir))


def cp_local(from_path, to_path):
    print("Copy from {} to {}".format(from_path, to_path))
    execute("cp -R {} {}".format(from_path, to_path))


def preload_screen(screen):
    print("Open {} screen".format(screen))
    execute("adb shell am start -a android.settings.{}".format(screen))


def turn_service(service, status):
    print("Turn {} {}".format(status, service))
    execute("adb shell settings put secure location_providers_allowed {}{}".format(status, service))
