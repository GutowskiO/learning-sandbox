package org.gutenn.trollplugin.listeners;

import org.bukkit.ChatColor;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;

public class PlayerJoinListener implements Listener {

    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent e) {

        Player p = e.getPlayer();
        String pName = p.getDisplayName();
        if (!p.hasPlayedBefore()) {
            e.setJoinMessage(ChatColor.DARK_GREEN + "" + ChatColor.BOLD + pName + " joined for the first time.");
        } else {
            e.setJoinMessage(ChatColor.DARK_GREEN + "" + ChatColor.BOLD  + pName + " joined the server.");
        }
    }
}
