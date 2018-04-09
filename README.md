# bin_packing_problem

final project in programing school

It's app written in Django Framework which try to solve packing problem in 1D(only weights).
First of all You need to by register/login user and then You can add/modify/delete elements/vehicle if You have right permissions.
After You add some elements and vehicle, app try to pack all elements into vehicles, starting from one with highest capacity.
If total wights of elements are greater then total capacity of vehicles there will by message that You need to add another vehicle or undo some elements.
If total wights of elements are lower then total capacity of vehicles then everything would be fine and final report will be shown,
where You will see used vehicles with their capacity and list of elements packed in specific vehicle with their total weights on this vehicle.