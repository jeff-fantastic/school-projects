extends Node2D

onready var ballNode = preload("res://Ball.tscn")
var ballWatch = false

func _process(_delta):
	if Input.is_action_just_pressed("ui_accept"): _spawn_ball()
	if Input.is_action_just_pressed("MESSAGE_TOGGLE"): $Controls.visible = not $Controls.visible
	if Input.is_action_just_pressed("BALL_WATCH"): _toggle_watch()
	_ball_watch()
func _spawn_ball():
	var ballInstance = ballNode.instance()
	ballInstance.global_position = get_global_mouse_position()
	get_tree().current_scene.add_child(ballInstance)

func _toggle_watch(): ballWatch = not ballWatch

func _ball_watch():
	if ballWatch:
		$CAM.zoom = lerp($CAM.zoom, Vector2(0.5, 0.5), 0.1)
		$CAM.global_position = lerp($CAM.global_position, 
									get_global_mouse_position(),
									0.1)
		$CAM.global_position.x = clamp($CAM.global_position.x, 25, 295)
		$CAM.global_position.y = clamp($CAM.global_position.y, 25, 215)
		$BALL_WATCH/INDICATOR.visible = true
	else:
		$CAM.zoom = lerp($CAM.zoom, Vector2(1,1), 0.1)
		$CAM.global_position = lerp($CAM.global_position, Vector2(160, 120), 0.1)
		$BALL_WATCH/INDICATOR.visible = false
