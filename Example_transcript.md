```
"C:\Users\Richard Pendrake\AppData\Local\Programs\Python\Python37\python.exe" "C:/Users/Richard Pendrake/PycharmProjects/cantina/viewtree_search_cli_demo_usage.py"
ViewTree Search
ViewTree Search CLI is a CLI which allows a user to load ViewTree JSON scripts from files or from URLs and then perform selector searches on it.
Type '\help' for instructions for use.
>>source
No JSON source is loaded.  Please load one from file or URL.
Remember: typing '\help' will get you instructions to use this CLI.
>>Input
No JSON source is loaded.  Please load one from file or URL.
Remember: typing '\help' will get you instructions to use this CLI.
>>@https://raw.githubusercontent.com/jdolan/quetoo/master/src/cgame/default/ui/settings/SystemViewController.json

Loaded source from  https://raw.githubusercontent.com/jdolan/quetoo/master/src/cgame/default/ui/settings/SystemViewController.json
>>>>Input
Match #1
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
Match #2
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
Match #3
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
Match #4
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
Match #5
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
Match #6
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
Match #7
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
Match #8
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
Match #9
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
Match #10
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
Match #11
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
Match #12
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
Match #13
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
Match #14
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
Match #15
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
Match #16
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
Match #17
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
Match #18
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
Match #19
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
Match #20
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
Match #21
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
Match #22
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
Match #23
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
Match #24
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
Match #25
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
Match #26
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
Found 0 entries
>>\source
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
Match #1
--------------------------------------------------------------------------------
{
    "class": "garindan",
    "classNames": [
        "container"
    ]
}
--------------------------------------------------------------------------------
Found 1 entry
>>source
Match #1
--------------------------------------------------------------------------------
{
    "class": "source",
    "classNames": [
        "help",
        "exit"
    ]
}
--------------------------------------------------------------------------------
Found 1 entry
>>#System.container
Match #1
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
Match #2
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
Found 0 entries
>>\exit
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
INFO:root:called:<class 'dict'>{'identifier': 'System', 'subviews': [{'class': 'StackView', 'classNames': ['container'], 'subviews': [{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'StackView', 'classNames': ['container'], 'subviews': [{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]}]
INFO:root:called:<class 'list'>[{'class': 'StackView', 'classNames': ['container'], 'subviews': [{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['container'], 'subviews': [{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]
INFO:root:called:<class 'list'>[{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]
INFO:root:called:<class 'list'>[{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]
INFO:root:called:<class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'VideoModeSelect', 'identifier': 'videoMode'}
INFO:root:called:<class 'dict'>{'class': 'VideoModeSelect', 'identifier': 'videoMode'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 2
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 3
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 4
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 2
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 3
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]
INFO:root:called:<class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 2
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 3
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 4
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 5
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 6
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 7
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 2
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]
INFO:root:called:<class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 2
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 3
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 4
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 's_reverse'}
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 's_reverse'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_download_maps'}
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_download_maps'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 2
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_download_models'}
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_download_models'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 3
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]
INFO:root:called:<class 'list'>[{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
Match #1
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
Match #2
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
Match #3
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
Match #4
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
Match #5
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
Match #6
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
Match #7
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
Match #8
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
Match #9
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
Match #10
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
Match #11
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
Match #12
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
Match #13
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
Match #14
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
Match #15
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
Match #16
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
Match #17
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
Match #18
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
Match #19
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
Match #20
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
Match #21
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
Match #22
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
Match #23
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
Match #24
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
Match #25
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
Match #26
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
INFO:root:string command: exit
INFO:root:['exit']
INFO:root:set()
INFO:root:command list['exit']
INFO:root:called:<class 'dict'>{'identifier': 'System', 'subviews': [{'class': 'StackView', 'classNames': ['container'], 'subviews': [{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'StackView', 'classNames': ['container'], 'subviews': [{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]}]
INFO:root:called:<class 'list'>[{'class': 'StackView', 'classNames': ['container'], 'subviews': [{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['container'], 'subviews': [{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]
INFO:root:called:<class 'list'>[{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}, {'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['columns', 'container'], 'subviews': [{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]
INFO:root:called:<class 'list'>[{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}, {'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]
INFO:root:called:<class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Display'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}, {'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}, {'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}, {'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}, {'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Video mode'}}, 'control': {'class': 'VideoModeSelect', 'identifier': 'videoMode'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'VideoModeSelect', 'identifier': 'videoMode'}
INFO:root:called:<class 'dict'>{'class': 'VideoModeSelect', 'identifier': 'videoMode'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'High DPI (4K)'}}, 'control': {'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 'r_allow_high_dpi'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 2
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Window mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'windowMode', 'var': 'r_fullscreen'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 3
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Vertical sync'}}, 'control': {'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'verticalSync', 'var': 'r_swap_interval'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 4
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Frame limiter'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 250, 'step': 5, 'var': 'cl_max_fps'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Rendering'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}, {'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}, {'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}, {'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Texture mode'}}, 'control': {'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'textureMode', 'expectsStringValue': True, 'var': 'r_texture_mode'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Anisotropy'}}, 'control': {'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'anisotropy', 'var': 'r_anisotropy'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 2
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Multisample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'multisample', 'var': 'r_multisample'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 3
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Supersample'}}, 'control': {'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'supersample', 'var': 'r_supersample'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]
INFO:root:called:<class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Picture'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}, {'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}, {'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}, {'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}, {'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}, {'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}, {'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}, {'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Brightness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_brightness'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Contrast'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_contrast'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 2
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Gamma'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_gamma'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 3
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Modulate'}}, 'control': {'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 1, 'max': 5, 'var': 'r_modulate'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 4
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Bumpmapping'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_bumpmap'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 5
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Hardness'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_hardness'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 6
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Specular'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_specular'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 7
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Parallax'}}, 'control': {'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0.1, 'max': 2, 'var': 'r_parallax'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 2
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['column', 'container'], 'subviews': [{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]
INFO:root:called:<class 'list'>[{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}, {'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Sound'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}, {'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Master'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_volume'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Effects'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_effects_volume'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 2
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Ambient'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_ambient_volume'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 3
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Music'}}, 'control': {'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}
INFO:root:called:<class 'dict'>{'class': 'CvarSlider', 'min': 0, 'max': 1, 'var': 's_music_volume'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 4
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Reverse stereo'}}, 'control': {'class': 'CvarCheckbox', 'var': 's_reverse'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 's_reverse'}
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 's_reverse'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Box', 'label': {'text': {'text': 'Network'}}, 'contentView': {'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}
INFO:root:called:<class 'dict'>{'subviews': [{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]
INFO:root:called:<class 'list'>[{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}, {'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}, {'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}, {'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Connection speed'}}, 'control': {'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}
INFO:root:called:<class 'dict'>{'class': 'CvarSelect', 'identifier': 'rate', 'var': 'rate'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Download maps'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_maps'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_download_maps'}
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_download_maps'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 2
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Download models'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_download_models'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_download_models'}
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_download_models'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 3
INFO:root:called:<class 'dict'>{'class': 'Input', 'label': {'text': {'text': 'Network graph'}}, 'control': {'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}
INFO:root:called:<class 'dict'>{'class': 'CvarCheckbox', 'var': 'cl_draw_net_graph'}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 1
INFO:root:called:<class 'dict'>{'class': 'StackView', 'classNames': ['accessoryView', 'container'], 'subviews': [{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:recursing into <class 'list'>[{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]
INFO:root:called:<class 'list'>[{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}]
INFO:root:found a list [not going to be a tuple or set]. searching it.
INFO:root:recursing list item [ 0
INFO:root:called:<class 'dict'>{'class': 'Button', 'identifier': 'apply', 'title': {'text': 'Apply'}}
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
INFO:root:found a dictionary.  searching it.
Found 0 entries
>>\exit
Are you sure?Yes, please

Process finished with exit code 0
``
