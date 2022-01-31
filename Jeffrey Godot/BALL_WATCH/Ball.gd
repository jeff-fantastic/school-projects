extends RigidBody2D

func _process(delta):
	if Input.is_action_pressed("MOUSE_HELD"):
		apply_central_impulse((get_global_mouse_position() - global_position).normalized() * 15)
	if Input.is_action_pressed("RMB_HELD"):
		apply_central_impulse((global_position - get_global_mouse_position()).normalized() * 15)
	if Input.is_action_just_pressed("ui_cancel"): queue_free()
	if global_position.x >= 340 || global_position.x <= -20: global_position = Vector2(160, 120)
	if global_position.y >= 260 || global_position.y <= -20: global_position = Vector2(160, 120)
