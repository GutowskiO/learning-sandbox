package org.gutenn.trollplugin.commands;

import org.bukkit.ChatColor;
import org.bukkit.Location;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.gutenn.trollplugin.TrollPlugin;

public class WorldSpawnCommand implements CommandExecutor {

    private TrollPlugin plugin;

    public WorldSpawnCommand(TrollPlugin plugin) {
        this.plugin = plugin;
    }

    @Override
    public boolean onCommand(CommandSender commandSender, Command command, String s, String[] strings) {

        if (commandSender instanceof Player p) {

            if (!p.hasPermission("permisssions.setwspawn")) {
                p.sendMessage(ChatColor.BOLD + "" +  ChatColor.DARK_RED + "Access Denied.");

                return true;
            }

            Location location = p.getLocation();
            plugin.getConfig().set("worldspawn", location);
            plugin.saveConfig();

            p.sendMessage("World spawn set!");

        }

        return true;
    }
}
