```
"C:\Users\Richard Pendrake\AppData\Local\Programs\Python\Python37\python.exe" "C:/Users/Richard Pendrake/PycharmProjects/cantina/viewtree_search_cli_demo_usage.py"
ViewTree Search
ViewTree Search CLI is a CLI which allows a user to load ViewTree JSON scripts from files or from URLs and then perform selector searches on it.
Type 'help' for instructions for use.
>>source
No JSON source has been loaded for viewtree searching
>>Input
No JSON source is loaded.  Please load one from file or URL.
Remember: typing 'help' will get you instructions to use this CLI.
>>@https://raw.githubusercontent.com/jdolan/quetoo/master/src/cgame/default/ui/settings/SystemViewController.json
Loaded source from  https://raw.githubusercontent.com/jdolan/quetoo/master/src/cgame/default/ui/settings/SystemViewController.json
>>Input
Finding 1
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Video mode"
        }
    },
    "control": {
        "class": "VideoModeSelect",
        "identifier": "videoMode"
    }
}
--------------------------------------------------------------------------------
Finding 2
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "High DPI (4K)"
        }
    },
    "control": {
        "class": "CvarCheckbox",
        "var": "r_allow_high_dpi"
    }
}
--------------------------------------------------------------------------------
Finding 3
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Window mode"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "windowMode",
        "var": "r_fullscreen"
    }
}
--------------------------------------------------------------------------------
Finding 4
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Vertical sync"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "verticalSync",
        "var": "r_swap_interval"
    }
}
--------------------------------------------------------------------------------
Finding 5
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Frame limiter"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0,
        "max": 250,
        "step": 5,
        "var": "cl_max_fps"
    }
}
--------------------------------------------------------------------------------
Finding 6
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Texture mode"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "textureMode",
        "expectsStringValue": true,
        "var": "r_texture_mode"
    }
}
--------------------------------------------------------------------------------
Finding 7
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Anisotropy"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "anisotropy",
        "var": "r_anisotropy"
    }
}
--------------------------------------------------------------------------------
Finding 8
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Multisample"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "multisample",
        "var": "r_multisample"
    }
}
--------------------------------------------------------------------------------
Finding 9
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Supersample"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "supersample",
        "var": "r_supersample"
    }
}
--------------------------------------------------------------------------------
Finding 10
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Brightness"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_brightness"
    }
}
--------------------------------------------------------------------------------
Finding 11
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Contrast"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_contrast"
    }
}
--------------------------------------------------------------------------------
Finding 12
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Gamma"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_gamma"
    }
}
--------------------------------------------------------------------------------
Finding 13
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Modulate"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 1,
        "max": 5,
        "var": "r_modulate"
    }
}
--------------------------------------------------------------------------------
Finding 14
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Bumpmapping"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_bumpmap"
    }
}
--------------------------------------------------------------------------------
Finding 15
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Hardness"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_hardness"
    }
}
--------------------------------------------------------------------------------
Finding 16
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Specular"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_specular"
    }
}
--------------------------------------------------------------------------------
Finding 17
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Parallax"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_parallax"
    }
}
--------------------------------------------------------------------------------
Finding 18
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Master"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0,
        "max": 1,
        "var": "s_volume"
    }
}
--------------------------------------------------------------------------------
Finding 19
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Effects"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0,
        "max": 1,
        "var": "s_effects_volume"
    }
}
--------------------------------------------------------------------------------
Finding 20
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Ambient"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0,
        "max": 1,
        "var": "s_ambient_volume"
    }
}
--------------------------------------------------------------------------------
Finding 21
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Music"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0,
        "max": 1,
        "var": "s_music_volume"
    }
}
--------------------------------------------------------------------------------
Finding 22
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Reverse stereo"
        }
    },
    "control": {
        "class": "CvarCheckbox",
        "var": "s_reverse"
    }
}
--------------------------------------------------------------------------------
Finding 23
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Connection speed"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "rate",
        "var": "rate"
    }
}
--------------------------------------------------------------------------------
Finding 24
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Download maps"
        }
    },
    "control": {
        "class": "CvarCheckbox",
        "var": "cl_download_maps"
    }
}
--------------------------------------------------------------------------------
Finding 25
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Download models"
        }
    },
    "control": {
        "class": "CvarCheckbox",
        "var": "cl_download_models"
    }
}
--------------------------------------------------------------------------------
Finding 26
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Network graph"
        }
    },
    "control": {
        "class": "CvarCheckbox",
        "var": "cl_draw_net_graph"
    }
}
--------------------------------------------------------------------------------
Found 26 entries
>>source
{
    "identifier": "System",
    "subviews": [
        {
            "class": "StackView",
            "classNames": [
                "container"
            ],
            "subviews": [
                {
                    "class": "StackView",
                    "classNames": [
                        "columns",
                        "container"
                    ],
                    "subviews": [
                        {
                            "class": "StackView",
                            "classNames": [
                                "column",
                                "container"
                            ],
                            "subviews": [
                                {
                                    "class": "Box",
                                    "label": {
                                        "text": {
                                            "text": "Display"
                                        }
                                    },
                                    "contentView": {
                                        "subviews": [
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Video mode"
                                                    }
                                                },
                                                "control": {
                                                    "class": "VideoModeSelect",
                                                    "identifier": "videoMode"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "High DPI (4K)"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarCheckbox",
                                                    "var": "r_allow_high_dpi"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Window mode"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "windowMode",
                                                    "var": "r_fullscreen"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Vertical sync"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "verticalSync",
                                                    "var": "r_swap_interval"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Frame limiter"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0,
                                                    "max": 250,
                                                    "step": 5,
                                                    "var": "cl_max_fps"
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    "class": "Box",
                                    "label": {
                                        "text": {
                                            "text": "Rendering"
                                        }
                                    },
                                    "contentView": {
                                        "subviews": [
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Texture mode"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "textureMode",
                                                    "expectsStringValue": true,
                                                    "var": "r_texture_mode"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Anisotropy"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "anisotropy",
                                                    "var": "r_anisotropy"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Multisample"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "multisample",
                                                    "var": "r_multisample"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Supersample"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "supersample",
                                                    "var": "r_supersample"
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        {
                            "class": "StackView",
                            "classNames": [
                                "column",
                                "container"
                            ],
                            "subviews": [
                                {
                                    "class": "Box",
                                    "label": {
                                        "text": {
                                            "text": "Picture"
                                        }
                                    },
                                    "contentView": {
                                        "subviews": [
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Brightness"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_brightness"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Contrast"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_contrast"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Gamma"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_gamma"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Modulate"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 1,
                                                    "max": 5,
                                                    "var": "r_modulate"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Bumpmapping"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_bumpmap"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Hardness"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_hardness"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Specular"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_specular"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Parallax"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_parallax"
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        {
                            "class": "StackView",
                            "classNames": [
                                "column",
                                "container"
                            ],
                            "subviews": [
                                {
                                    "class": "Box",
                                    "label": {
                                        "text": {
                                            "text": "Sound"
                                        }
                                    },
                                    "contentView": {
                                        "subviews": [
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Master"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0,
                                                    "max": 1,
                                                    "var": "s_volume"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Effects"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0,
                                                    "max": 1,
                                                    "var": "s_effects_volume"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Ambient"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0,
                                                    "max": 1,
                                                    "var": "s_ambient_volume"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Music"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0,
                                                    "max": 1,
                                                    "var": "s_music_volume"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Reverse stereo"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarCheckbox",
                                                    "var": "s_reverse"
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    "class": "Box",
                                    "label": {
                                        "text": {
                                            "text": "Network"
                                        }
                                    },
                                    "contentView": {
                                        "subviews": [
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Connection speed"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "rate",
                                                    "var": "rate"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Download maps"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarCheckbox",
                                                    "var": "cl_download_maps"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Download models"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarCheckbox",
                                                    "var": "cl_download_models"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Network graph"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarCheckbox",
                                                    "var": "cl_draw_net_graph"
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "class": "StackView",
                    "classNames": [
                        "accessoryView",
                        "container"
                    ],
                    "subviews": [
                        {
                            "class": "Button",
                            "identifier": "apply",
                            "title": {
                                "text": "Apply"
                            }
                        }
                    ]
                }
            ]
        }
    ]
}
>>garindan
Found 0 entries
>>!mos_eisley.json
Loaded source from  mos_eisley.json
>>garindan
Finding 1
--------------------------------------------------------------------------------
{
    "class": "garindan",
    "classNames": [
        "container"
    ]
}
--------------------------------------------------------------------------------
Found 1 entry
>>#System.container
Finding 1
--------------------------------------------------------------------------------
{
    "class": "StackView",
    "classNames": [
        "container"
    ],
    "subviews": [
        {
            "label": {
                "control": {
                    "class": "CvarCheckbox",
                    "var": "cl_download_models"
                }
            }
        },
        {
            "class": "garindan",
            "classNames": [
                "container"
            ]
        }
    ]
}
--------------------------------------------------------------------------------
Finding 2
--------------------------------------------------------------------------------
{
    "class": "garindan",
    "classNames": [
        "container"
    ]
}
--------------------------------------------------------------------------------
Found 2 entries
>>exit
Are you sure?No way!
Exit attempt cancelled.  Resuming CLI
JSON source data is still loaded from before
>>CvarCheckbox
Found 0 entries
>>?
Debug mode enabled.
>>@https://raw.githubusercontent.com/jdolan/quetoo/master/src/cgame/default/ui/settings/SystemViewController.json
Loaded source from  https://raw.githubusercontent.com/jdolan/quetoo/master/src/cgame/default/ui/settings/SystemViewController.json
Source:  {
    "identifier": "System",
    "subviews": [
        {
            "class": "StackView",
            "classNames": [
                "container"
            ],
            "subviews": [
                {
                    "class": "StackView",
                    "classNames": [
                        "columns",
                        "container"
                    ],
                    "subviews": [
                        {
                            "class": "StackView",
                            "classNames": [
                                "column",
                                "container"
                            ],
                            "subviews": [
                                {
                                    "class": "Box",
                                    "label": {
                                        "text": {
                                            "text": "Display"
                                        }
                                    },
                                    "contentView": {
                                        "subviews": [
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Video mode"
                                                    }
                                                },
                                                "control": {
                                                    "class": "VideoModeSelect",
                                                    "identifier": "videoMode"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "High DPI (4K)"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarCheckbox",
                                                    "var": "r_allow_high_dpi"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Window mode"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "windowMode",
                                                    "var": "r_fullscreen"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Vertical sync"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "verticalSync",
                                                    "var": "r_swap_interval"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Frame limiter"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0,
                                                    "max": 250,
                                                    "step": 5,
                                                    "var": "cl_max_fps"
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    "class": "Box",
                                    "label": {
                                        "text": {
                                            "text": "Rendering"
                                        }
                                    },
                                    "contentView": {
                                        "subviews": [
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Texture mode"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "textureMode",
                                                    "expectsStringValue": true,
                                                    "var": "r_texture_mode"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Anisotropy"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "anisotropy",
                                                    "var": "r_anisotropy"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Multisample"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "multisample",
                                                    "var": "r_multisample"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Supersample"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "supersample",
                                                    "var": "r_supersample"
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        {
                            "class": "StackView",
                            "classNames": [
                                "column",
                                "container"
                            ],
                            "subviews": [
                                {
                                    "class": "Box",
                                    "label": {
                                        "text": {
                                            "text": "Picture"
                                        }
                                    },
                                    "contentView": {
                                        "subviews": [
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Brightness"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_brightness"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Contrast"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_contrast"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Gamma"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_gamma"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Modulate"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 1,
                                                    "max": 5,
                                                    "var": "r_modulate"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Bumpmapping"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_bumpmap"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Hardness"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_hardness"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Specular"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_specular"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Parallax"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0.1,
                                                    "max": 2,
                                                    "var": "r_parallax"
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        },
                        {
                            "class": "StackView",
                            "classNames": [
                                "column",
                                "container"
                            ],
                            "subviews": [
                                {
                                    "class": "Box",
                                    "label": {
                                        "text": {
                                            "text": "Sound"
                                        }
                                    },
                                    "contentView": {
                                        "subviews": [
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Master"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0,
                                                    "max": 1,
                                                    "var": "s_volume"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Effects"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0,
                                                    "max": 1,
                                                    "var": "s_effects_volume"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Ambient"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0,
                                                    "max": 1,
                                                    "var": "s_ambient_volume"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Music"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSlider",
                                                    "min": 0,
                                                    "max": 1,
                                                    "var": "s_music_volume"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Reverse stereo"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarCheckbox",
                                                    "var": "s_reverse"
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    "class": "Box",
                                    "label": {
                                        "text": {
                                            "text": "Network"
                                        }
                                    },
                                    "contentView": {
                                        "subviews": [
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Connection speed"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarSelect",
                                                    "identifier": "rate",
                                                    "var": "rate"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Download maps"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarCheckbox",
                                                    "var": "cl_download_maps"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Download models"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarCheckbox",
                                                    "var": "cl_download_models"
                                                }
                                            },
                                            {
                                                "class": "Input",
                                                "label": {
                                                    "text": {
                                                        "text": "Network graph"
                                                    }
                                                },
                                                "control": {
                                                    "class": "CvarCheckbox",
                                                    "var": "cl_draw_net_graph"
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "class": "StackView",
                    "classNames": [
                        "accessoryView",
                        "container"
                    ],
                    "subviews": [
                        {
                            "class": "Button",
                            "identifier": "apply",
                            "title": {
                                "text": "Apply"
                            }
                        }
                    ]
                }
            ]
        }
    ]
}
>>Input
INFO:root:string command: Input
INFO:root:['Input']
INFO:root:set()
INFO:root:command list['Input']
INFO:root:Level0
INFO:root:called:<class 'dict'>{'identifier': 'System', 'subviews': [{'class': 'StackView', 'classNames': ['container'], 'subviews': [{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'StackView', 'classNames': ['container'], 'subviews': [{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]}]
INFO:root:Level1
INFO:root:called:<class 'list'>[{'class': 'StackView', 'classNames': ['container'], 'subviews': [{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]}]
INFO:root:found a list.  searching it.
INFO:root:recursing list item [ 0
INFO:root:Level2
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['container'], 'subviews': [{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]
INFO:root:Level3
INFO:root:called:<class 'list'>[{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]
INFO:root:found a list.  searching it.
INFO:root:recursing list item [ 0
INFO:root:Level4
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]
INFO:root:Level5
INFO:root:called:<class 'list'>[{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]
INFO:root:found a list.  searching it.
INFO:root:recursing list item [ 0
INFO:root:Level6
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]
INFO:root:Level7
INFO:root:called:<class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]
INFO:root:found a list.  searching it.
INFO:root:recursing list item [ 0
INFO:root:Level8
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}
INFO:root:Level9
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]
INFO:root:Level10
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]
INFO:root:found a list.  searching it.
INFO:root:recursing list item [ 0
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'VideoModeSelect', 'identifier': 'videoMode'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'VideoModeSelect', 'identifier': 'videoMode'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 1
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 2
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 3
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 4
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 1
INFO:root:Level8
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}
INFO:root:Level9
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]
INFO:root:Level10
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]
INFO:root:found a list.  searching it.
INFO:root:recursing list item [ 0
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 1
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 2
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 3
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 1
INFO:root:Level6
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]
INFO:root:Level7
INFO:root:called:<class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]
INFO:root:found a list.  searching it.
INFO:root:recursing list item [ 0
INFO:root:Level8
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}
INFO:root:Level9
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]
INFO:root:Level10
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]
INFO:root:found a list.  searching it.
INFO:root:recursing list item [ 0
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 1
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 2
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 3
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 4
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 5
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 6
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 7
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 2
INFO:root:Level6
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]
INFO:root:Level7
INFO:root:called:<class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]
INFO:root:found a list.  searching it.
INFO:root:recursing list item [ 0
INFO:root:Level8
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}
INFO:root:Level9
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]
INFO:root:Level10
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]
INFO:root:found a list.  searching it.
INFO:root:recursing list item [ 0
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 1
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 2
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 3
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 4
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 's_reverse'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 's_reverse'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 1
INFO:root:Level8
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}
INFO:root:Level9
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]
INFO:root:Level10
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]
INFO:root:found a list.  searching it.
INFO:root:recursing list item [ 0
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 1
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_download_maps'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_download_maps'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 2
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_download_models'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_download_models'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 3
INFO:root:Level11
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}
INFO:root:Level12
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing list item [ 1
INFO:root:Level4
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]
INFO:root:Level5
INFO:root:called:<class 'list'>[{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]
INFO:root:found a list.  searching it.
INFO:root:recursing list item [ 0
INFO:root:Level6
INFO:root:called:<class 'dict'>{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}
INFO:root:found a dictionary.  searching it.
Finding 1
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Video mode"
        }
    },
    "control": {
        "class": "VideoModeSelect",
        "identifier": "videoMode"
    }
}
--------------------------------------------------------------------------------
Finding 2
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "High DPI (4K)"
        }
    },
    "control": {
        "class": "CvarCheckbox",
        "var": "r_allow_high_dpi"
    }
}
--------------------------------------------------------------------------------
Finding 3
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Window mode"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "windowMode",
        "var": "r_fullscreen"
    }
}
--------------------------------------------------------------------------------
Finding 4
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Vertical sync"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "verticalSync",
        "var": "r_swap_interval"
    }
}
--------------------------------------------------------------------------------
Finding 5
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Frame limiter"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0,
        "max": 250,
        "step": 5,
        "var": "cl_max_fps"
    }
}
--------------------------------------------------------------------------------
Finding 6
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Texture mode"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "textureMode",
        "expectsStringValue": true,
        "var": "r_texture_mode"
    }
}
--------------------------------------------------------------------------------
Finding 7
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Anisotropy"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "anisotropy",
        "var": "r_anisotropy"
    }
}
--------------------------------------------------------------------------------
Finding 8
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Multisample"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "multisample",
        "var": "r_multisample"
    }
}
--------------------------------------------------------------------------------
Finding 9
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Supersample"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "supersample",
        "var": "r_supersample"
    }
}
--------------------------------------------------------------------------------
Finding 10
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Brightness"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_brightness"
    }
}
--------------------------------------------------------------------------------
Finding 11
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Contrast"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_contrast"
    }
}
--------------------------------------------------------------------------------
Finding 12
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Gamma"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_gamma"
    }
}
--------------------------------------------------------------------------------
Finding 13
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Modulate"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 1,
        "max": 5,
        "var": "r_modulate"
    }
}
--------------------------------------------------------------------------------
Finding 14
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Bumpmapping"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_bumpmap"
    }
}
--------------------------------------------------------------------------------
Finding 15
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Hardness"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_hardness"
    }
}
--------------------------------------------------------------------------------
Finding 16
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Specular"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_specular"
    }
}
--------------------------------------------------------------------------------
Finding 17
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Parallax"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0.1,
        "max": 2,
        "var": "r_parallax"
    }
}
--------------------------------------------------------------------------------
Finding 18
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Master"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0,
        "max": 1,
        "var": "s_volume"
    }
}
--------------------------------------------------------------------------------
Finding 19
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Effects"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0,
        "max": 1,
        "var": "s_effects_volume"
    }
}
--------------------------------------------------------------------------------
Finding 20
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Ambient"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0,
        "max": 1,
        "var": "s_ambient_volume"
    }
}
--------------------------------------------------------------------------------
Finding 21
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Music"
        }
    },
    "control": {
        "class": "CvarSlider",
        "min": 0,
        "max": 1,
        "var": "s_music_volume"
    }
}
--------------------------------------------------------------------------------
Finding 22
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Reverse stereo"
        }
    },
    "control": {
        "class": "CvarCheckbox",
        "var": "s_reverse"
    }
}
--------------------------------------------------------------------------------
Finding 23
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Connection speed"
        }
    },
    "control": {
        "class": "CvarSelect",
        "identifier": "rate",
        "var": "rate"
    }
}
--------------------------------------------------------------------------------
Finding 24
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Download maps"
        }
    },
    "control": {
        "class": "CvarCheckbox",
        "var": "cl_download_maps"
    }
}
--------------------------------------------------------------------------------
Finding 25
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Download models"
        }
    },
    "control": {
        "class": "CvarCheckbox",
        "var": "cl_download_models"
    }
}
--------------------------------------------------------------------------------
Finding 26
--------------------------------------------------------------------------------
{
    "class": "Input",
    "label": {
        "text": {
            "text": "Network graph"
        }
    },
    "control": {
        "class": "CvarCheckbox",
        "var": "cl_draw_net_graph"
    }
}
--------------------------------------------------------------------------------
Found 26 entries
>>exit
Are you sure?Yes, please

Process finished with exit code 0
```
