#!/bin/bash
echo "$(glxinfo | grep Device | tail -n1 | awk '{print $2}')"

# will print result like `Mali G52` or `Mali T860` - package "mesa-utils" is required for `glxinfo`