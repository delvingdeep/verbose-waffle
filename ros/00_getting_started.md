## ROS Basics
All the instructions assumes ROS Kinetic Kame full desktop version already installed.

To source environment after installing anything using apt-get
- `source /opt/ros/kinetic/setup.bash`

---

##### Create a catkin workspace
To create and build catkin workspace
```bash
mkdir -p catkin_ws/src
catkin_init_worksapce
cd catkin_ws/
catkin_make
```

To source workspace :
```bash
source devel/setup.bash
```

To make sure workspace have been properly overlayed :
```bash
echo $ROS_PACKAGE_PATH
```
output should show workspace directory along with `(CATKIN_WORKSAPCE_DIR):/opt/ros/kinetic/share`

---

#### Create a catkin Package
To create a catkin Package
```bash
cd catkin_ws/src
catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
```
Next step is to build the workspace with new package, change directory to `catkin_ws/`
```bash
cd ..
catkin_make
```
Add updated workspace to the ROS environment
```bash
source devel/setup.bash
```

---

